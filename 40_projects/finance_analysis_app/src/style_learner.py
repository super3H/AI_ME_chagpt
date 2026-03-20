from __future__ import annotations

import re
from pathlib import Path

from src.llm import get_client, has_openai_key, json_response
from src.models import StyleProfile
from src.storage import read_json, write_json


class StyleLearner:
    def __init__(self, profile_path: Path) -> None:
        self.profile_path = profile_path

    def load(self) -> StyleProfile:
        data = read_json(self.profile_path, {})
        return StyleProfile.from_dict(data)

    def save(self, profile: StyleProfile) -> None:
        write_json(self.profile_path, profile.to_dict())

    def learn_from_text(self, text: str) -> StyleProfile:
        profile = self.load()
        extracted = self._extract_style(text)
        profile.merge(extracted)
        self.save(profile)
        return profile

    def _extract_style(self, text: str) -> dict:
        if has_openai_key():
            prompt = f"""
你是金融研究方法抽取器。请从下面文本中提取分析风格，输出 JSON：
{{
  "risk_preference": "保守|平衡|激进",
  "horizon": "短期|中期|长期",
  "focus_sectors": ["行业1", "行业2"],
  "preferred_factors": ["因子1", "因子2"],
  "reasoning_patterns": ["推理习惯1", "推理习惯2"],
  "watch_signals": ["预警信号1", "预警信号2"]
}}

文本：
\"\"\"{text}\"\"\"
"""
            client = get_client()
            return json_response(client, prompt)
        return _rule_based_style_extract(text)


def _rule_based_style_extract(text: str) -> dict:
    low = text.lower()
    risk = "平衡"
    if any(k in low for k in ["止损", "防守", "低波", "保守", "风险控制"]):
        risk = "保守"
    if any(k in low for k in ["进攻", "高弹性", "激进", "加杠杆", "高beta"]):
        risk = "激进"

    horizon = "中期"
    if any(k in text for k in ["日内", "短线", "周内", "事件驱动"]):
        horizon = "短期"
    if any(k in text for k in ["年度", "长期", "三年", "五年", "周期"]):
        horizon = "长期"

    sectors = _match_keywords(
        text,
        [
            "半导体",
            "AI",
            "新能源",
            "医药",
            "消费",
            "银行",
            "券商",
            "房地产",
            "军工",
            "港口航运",
            "黄金",
            "原油",
        ],
    )

    factors = _match_keywords(
        text,
        ["估值", "盈利", "现金流", "政策", "利率", "汇率", "通胀", "库存", "供需", "资金面", "情绪"],
    )

    patterns = []
    if "先" in text and "再" in text:
        patterns.append("分阶段推演")
    if any(k in text for k in ["如果", "则", "否则"]):
        patterns.append("条件分支判断")
    if re.search(r"\d+(\.\d+)?%", text):
        patterns.append("量化阈值驱动")
    if not patterns:
        patterns.append("基本面与事件结合")

    watch_signals = _match_keywords(
        text,
        ["财报不及预期", "政策转向", "流动性收紧", "地缘冲突", "美元走强", "信用风险", "出口下滑"],
    )

    return {
        "risk_preference": risk,
        "horizon": horizon,
        "focus_sectors": sectors,
        "preferred_factors": factors,
        "reasoning_patterns": patterns,
        "watch_signals": watch_signals,
    }


def _match_keywords(text: str, keywords: list[str]) -> list[str]:
    return [k for k in keywords if k.lower() in text.lower()]
