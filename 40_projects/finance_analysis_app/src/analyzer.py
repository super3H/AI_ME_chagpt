from __future__ import annotations

from dataclasses import asdict

from src.llm import get_client, has_openai_key, text_response
from src.models import StyleProfile
from src.news import NewsItem


def generate_analysis(
    user_input: str,
    profile: StyleProfile,
    news_items: list[NewsItem],
    symbols: list[str],
) -> str:
    if has_openai_key():
        return _llm_analysis(user_input, profile, news_items, symbols)
    return _rule_based_analysis(user_input, profile, news_items, symbols)


def _llm_analysis(
    user_input: str,
    profile: StyleProfile,
    news_items: list[NewsItem],
    symbols: list[str],
) -> str:
    client = get_client()
    news_block = "\n".join(
        [
            f"- [{item.published}] {item.title} | {item.source}\n  链接: {item.link}"
            for item in news_items[:12]
        ]
    )
    prompt = f"""
你是资深买方研究员。你的任务是基于用户输入、已学习到的分析风格、和最新新闻，输出“需要关注的方向”。
请使用中文，结构必须包含：
1) 市场主线（3-5条）
2) 重点跟踪清单（按优先级，含触发条件）
3) 风险清单（含预警指标）
4) 48小时行动建议（可执行）

用户输入：
{user_input}

关注标的/关键词：
{", ".join(symbols) if symbols else "未指定"}

已学习风格：
{asdict(profile)}

最新新闻：
{news_block if news_block else "暂无新闻"}
"""
    return text_response(client, prompt)


def _rule_based_analysis(
    user_input: str,
    profile: StyleProfile,
    news_items: list[NewsItem],
    symbols: list[str],
) -> str:
    top_news = news_items[:5]
    lines = []
    lines.append("1) 市场主线")
    if profile.focus_sectors:
        lines.append(f"- 优先看 {', '.join(profile.focus_sectors[:5])}，符合已学习风格。")
    else:
        lines.append("- 优先从政策、流动性和盈利预期三条线并行跟踪。")
    if symbols:
        lines.append(f"- 重点标的/关键词：{', '.join(symbols)}。")
    lines.append("")
    lines.append("2) 重点跟踪清单")
    lines.append("- 跟踪宏观：利率、汇率、通胀预期变化。")
    lines.append("- 跟踪行业：龙头财报、订单和库存数据。")
    if top_news:
        for item in top_news:
            lines.append(f"- 新闻事件：{item.title}（{item.source}，{item.published}）。")
    lines.append("")
    lines.append("3) 风险清单")
    if profile.watch_signals:
        for signal in profile.watch_signals[:6]:
            lines.append(f"- 预警信号：{signal}。")
    else:
        lines.append("- 预警信号：流动性收紧、政策不及预期、盈利下修。")
    lines.append("")
    lines.append("4) 48小时行动建议")
    lines.append("- 复核近7日新闻与持仓相关性，更新事件优先级。")
    lines.append("- 设定触发阈值（价格/成交量/政策时间点）并分批执行。")
    if user_input.strip():
        lines.append("- 将本次输入加入样本库，持续学习你的判断框架。")
    return "\n".join(lines)
