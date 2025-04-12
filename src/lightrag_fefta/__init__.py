"""LightRag FEFTA package."""

import os
import asyncio
from dotenv import load_dotenv
from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed
from lightrag.kg.shared_storage import initialize_pipeline_status
from lightrag.utils import setup_logger

__version__ = "0.1.0"

setup_logger("lightrag", level="INFO")

# 環境変数のロード
load_dotenv()

async def initialize_rag():
    """Initialize RAG instance."""
    rag = LightRAG(
        working_dir="./lightrag_data",
        embedding_func=openai_embed,
        llm_model_func=gpt_4o_mini_complete
    )

    await rag.initialize_storages()
    await initialize_pipeline_status()

    return rag

def main() -> None:
    """Run the main program."""
    # Initialize RAG instance
    rag = asyncio.run(initialize_rag())

    # サンプルドキュメントを追加
    documents = [
        "東京は日本の首都です。",
        "富士山は日本一高い山です。",
        "京都には多くの寺社仏閣があります。"
    ]
    for doc in documents:
        rag.insert(doc)

    # 様々なモードでクエリを実行
    query = "日本の首都について教えてください。"
    modes = ["naive", "local", "global", "hybrid", "mix"]

    for mode in modes:
        print(f"\nMode: {mode}")
        result = rag.query(query, param=QueryParam(mode=mode))
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
