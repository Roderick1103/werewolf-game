from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class DeepSeekConfig:
    api_key: str | None
    model: str
    base_url: str

    @property
    def is_ready(self) -> bool:
        return bool(self.api_key)


def load_config() -> DeepSeekConfig:
    load_dotenv()
    return DeepSeekConfig(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        model=os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash"),
        base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
    )
