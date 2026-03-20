from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from urllib.parse import quote

import feedparser


@dataclass
class NewsItem:
    title: str
    source: str
    published: str
    link: str
    summary: str


def fetch_google_finance_news(keywords: list[str], limit_per_keyword: int = 5) -> list[NewsItem]:
    results: list[NewsItem] = []
    seen_links: set[str] = set()

    for keyword in keywords:
        query = quote(f"{keyword} finance market")
        url = f"https://news.google.com/rss/search?q={query}&hl=zh-CN&gl=CN&ceid=CN:zh-Hans"
        feed = feedparser.parse(url)
        for entry in feed.entries[:limit_per_keyword]:
            link = getattr(entry, "link", "")
            if not link or link in seen_links:
                continue
            seen_links.add(link)
            published = _format_published(entry)
            results.append(
                NewsItem(
                    title=getattr(entry, "title", "无标题"),
                    source=_extract_source(entry),
                    published=published,
                    link=link,
                    summary=getattr(entry, "summary", "").strip(),
                )
            )
    return sorted(results, key=lambda x: x.published, reverse=True)[:20]


def _extract_source(entry: feedparser.FeedParserDict) -> str:
    source = getattr(entry, "source", None)
    if source and isinstance(source, dict):
        return source.get("title", "未知来源")
    return "未知来源"


def _format_published(entry: feedparser.FeedParserDict) -> str:
    dt_tuple = getattr(entry, "published_parsed", None) or getattr(entry, "updated_parsed", None)
    if not dt_tuple:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return datetime(*dt_tuple[:6]).strftime("%Y-%m-%d %H:%M:%S")
