from __future__ import annotations

from .config import load_config
from .deepseek import create_deepseek_llm


def main() -> None:
    config = load_config()
    print("DeepSeek 配置")
    print(f"模型: {config.model}")
    print(f"接口地址: {config.base_url}")
    print(f"API Key: {'已配置' if config.is_ready else '未配置'}")

    if not config.is_ready:
        raise SystemExit("请先在 .env 中配置 DEEPSEEK_API_KEY。")

    llm = create_deepseek_llm(config, temperature=0)
    response = llm.invoke("只回复两个字：正常")
    print(f"连接测试: {response.content}")


if __name__ == "__main__":
    main()
