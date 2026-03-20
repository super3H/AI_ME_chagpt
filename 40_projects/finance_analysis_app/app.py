from __future__ import annotations

from datetime import datetime
from pathlib import Path

import streamlit as st

from src.analyzer import generate_analysis
from src.llm import get_client, has_openai_key, to_text_from_image
from src.news import fetch_google_finance_news
from src.style_learner import StyleLearner

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
CASES_DIR = DATA_DIR / "cases"
PROFILE_PATH = DATA_DIR / "style_profile.json"

learner = StyleLearner(PROFILE_PATH)


def main() -> None:
    st.set_page_config(page_title="金融分析助手", page_icon=":chart_with_upwards_trend:", layout="wide")
    st.title("金融分析应用（图片 + 文字 + 新闻）")
    st.caption("目标：学习你的分析思维，并结合最新新闻输出重点关注方向。")

    profile = learner.load()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("已学习风格")
        st.json(profile.to_dict())
    with col2:
        st.subheader("使用状态")
        st.write(f"- OpenAI Key: {'已配置' if has_openai_key() else '未配置（将使用本地规则模式）'}")
        st.write("- 新闻源：Google News RSS（实时抓取）")

    tab_learn, tab_analyze = st.tabs(["1) 学习样本", "2) 生成分析"])

    with tab_learn:
        learn_text = st.text_area(
            "输入你的分析样本（文字）",
            height=220,
            placeholder="例如：先看美债利率，再看AI链条业绩兑现...",
        )
        learn_images = st.file_uploader(
            "上传样本图片（研报截图/笔记）",
            type=["png", "jpg", "jpeg", "webp"],
            accept_multiple_files=True,
            key="learn_images",
        )

        if st.button("从图片提取文字（学习区）"):
            extracted = extract_texts_from_images(learn_images)
            st.session_state["learn_extracted_text"] = "\n\n".join(extracted)
            st.text_area("图片提取结果", st.session_state["learn_extracted_text"], height=180)

        if st.button("学习这些样本"):
            image_text = st.session_state.get("learn_extracted_text", "")
            merged_text = "\n\n".join([learn_text.strip(), image_text.strip()]).strip()
            if not merged_text:
                st.warning("请至少提供文字或图片提取内容。")
            else:
                new_profile = learner.learn_from_text(merged_text)
                save_case("learn_sample", merged_text)
                st.success("学习完成，风格已更新。")
                st.json(new_profile.to_dict())

    with tab_analyze:
        input_text = st.text_area(
            "输入本次待分析内容",
            height=220,
            placeholder="例如：我关注A股算力和半导体，担心海外利率超预期上行...",
        )
        analyze_images = st.file_uploader(
            "上传本次分析图片",
            type=["png", "jpg", "jpeg", "webp"],
            accept_multiple_files=True,
            key="analyze_images",
        )
        symbols_raw = st.text_input("关注标的/关键词（逗号分隔）", value="")
        extra_keywords_raw = st.text_input("新闻关键词（可选，逗号分隔）", value="")

        if st.button("从图片提取文字（分析区）"):
            extracted = extract_texts_from_images(analyze_images)
            st.session_state["analyze_extracted_text"] = "\n\n".join(extracted)
            st.text_area("图片提取结果", st.session_state["analyze_extracted_text"], height=180)

        if st.button("生成关注方向", type="primary"):
            image_text = st.session_state.get("analyze_extracted_text", "")
            merged_input = "\n\n".join([input_text.strip(), image_text.strip()]).strip()
            symbols = parse_csv(symbols_raw)
            extra_keywords = parse_csv(extra_keywords_raw)
            news_keywords = _build_news_keywords(symbols, extra_keywords, profile.focus_sectors)

            with st.spinner("抓取新闻并生成分析中..."):
                news_items = fetch_google_finance_news(news_keywords or ["宏观经济", "股市", "债券"])
                analysis = generate_analysis(merged_input, profile, news_items, symbols)

            save_case("analysis_case", merged_input)
            st.subheader("分析结果")
            st.markdown(analysis)

            st.subheader("抓取到的新闻（用于本次分析）")
            for item in news_items[:12]:
                st.markdown(f"- {item.published} | {item.source} | [{item.title}]({item.link})")


def extract_texts_from_images(uploaded_files: list | None) -> list[str]:
    if not uploaded_files:
        return []

    if not has_openai_key():
        return ["未配置 OPENAI_API_KEY，无法解析图片；请先配置后重试。"]

    client = get_client()
    extracted: list[str] = []
    for file in uploaded_files:
        content = file.read()
        if not content:
            continue
        mime_type = file.type or "image/png"
        try:
            text = to_text_from_image(client, content, mime_type)
            if text:
                extracted.append(f"[{file.name}]\n{text}")
        except Exception as ex:
            extracted.append(f"[{file.name}] 提取失败: {ex}")
    return extracted


def parse_csv(text: str) -> list[str]:
    return [item.strip() for item in text.split(",") if item.strip()]


def _build_news_keywords(symbols: list[str], extra: list[str], sectors: list[str]) -> list[str]:
    merged = []
    for token in [*symbols, *extra, *sectors]:
        token = token.strip()
        if token and token not in merged:
            merged.append(token)
    return merged[:8]


def save_case(prefix: str, content: str) -> None:
    CASES_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file = CASES_DIR / f"{prefix}_{timestamp}.md"
    file.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
