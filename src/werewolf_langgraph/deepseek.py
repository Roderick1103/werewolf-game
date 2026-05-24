from __future__ import annotations

from langchain_openai import ChatOpenAI

from .config import DeepSeekConfig


def create_deepseek_llm(config: DeepSeekConfig, temperature: float = 0.2) -> ChatOpenAI:
    if not config.is_ready:
        raise ValueError("DEEPSEEK_API_KEY is not configured.")

    return ChatOpenAI(
        api_key=config.api_key,
        base_url=config.base_url,
        model=config.model,
        temperature=temperature,
    )
