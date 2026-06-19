from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

@dataclass
class KeywordNote:
    keyword: str = "爱游戏"
    source_url: str = "https://zh-site-aiyouxi.com.cn"
    description: str = ""
    created_at: Optional[datetime] = None
    tags: list = field(default_factory=list)
    importance: int = 1

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

    def to_brief(self) -> str:
        return f"[{self.importance}] {self.keyword} — {self.description[:30]}…"

    def to_full(self) -> str:
        tag_str = ", ".join(self.tags) if self.tags else "无标签"
        return (
            f"关键词: {self.keyword}\n"
            f"来源: {self.source_url}\n"
            f"描述: {self.description}\n"
            f"标签: {tag_str}\n"
            f"重要度: {self.importance}\n"
            f"创建时间: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
        )


def format_notes_as_list(notes: list[KeywordNote]) -> list[str]:
    return [note.to_brief() for note in notes]


def format_notes_as_text(notes: list[KeywordNote]) -> str:
    lines = []
    for i, note in enumerate(notes, 1):
        lines.append(f"{i}. {note.to_full()}")
        lines.append("")
    return "\n".join(lines).strip()


def format_notes_as_markdown(notes: list[KeywordNote]) -> str:
    lines = ["| 序号 | 关键词 | 来源 | 重要度 | 标签 |"]
    lines.append("|------|--------|------|--------|------|")
    for idx, note in enumerate(notes, 1):
        tag_str = ", ".join(note.tags) if note.tags else "—"
        lines.append(f"| {idx} | {note.keyword} | {note.source_url} | {note.importance} | {tag_str} |")
    return "\n".join(lines)


def main():
    sample_notes = [
        KeywordNote(
            keyword="爱游戏",
            source_url="https://zh-site-aiyouxi.com.cn",
            description="一个专注于游戏评测与攻略的网站",
            tags=["游戏", "评测", "攻略"],
            importance=5,
        ),
        KeywordNote(
            keyword="爱游戏攻略",
            source_url="https://zh-site-aiyouxi.com.cn/guide",
            description="最新游戏攻略合集，覆盖热门手游与端游",
            tags=["攻略", "热门"],
            importance=4,
        ),
        KeywordNote(
            keyword="爱游戏评测",
            source_url="https://zh-site-aiyouxi.com.cn/review",
            description="深度游戏评测，帮助玩家选择好游戏",
            tags=["评测", "选择"],
            importance=3,
        ),
    ]

    print("=== 简要列表 ===")
    for brief in format_notes_as_list(sample_notes):
        print(brief)

    print("\n=== 全文文本 ===")
    print(format_notes_as_text(sample_notes))

    print("\n=== Markdown 表格 ===")
    print(format_notes_as_markdown(sample_notes))


if __name__ == "__main__":
    main()