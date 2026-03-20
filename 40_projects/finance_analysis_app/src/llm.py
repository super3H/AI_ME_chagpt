from __future__ import annotations

import base64
import json
import os
import re
from typing import Any

from openai import OpenAI


def has_openai_key() -> bool:
    return bool(os.getenv("OPENAI_API_KEY"))


def get_client() -> OpenAI:
    return OpenAI()


def to_text_from_image(client: OpenAI, image_bytes: bytes, mime_type: str) -> str:
    b64 = base64.b64encode(image_bytes).decode("utf-8")
    result = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": "请提取这张图片中与金融分析相关的文字和要点。只返回提取结果。"},
                    {
                        "type": "input_image",
                        "image_url": f"data:{mime_type};base64,{b64}",
                    },
                ],
            }
        ],
    )
    return result.output_text.strip()


def json_response(client: OpenAI, prompt: str) -> dict[str, Any]:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[{"role": "user", "content": prompt}],
    )
    text = response.output_text.strip()
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError(f"无法解析 JSON: {text[:200]}")
    return json.loads(match.group(0))


def text_response(client: OpenAI, prompt: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[{"role": "user", "content": prompt}],
    )
    return response.output_text.strip()
