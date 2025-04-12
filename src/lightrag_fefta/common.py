"""Common utilities for LightRag FEFTA."""

import os
import asyncio
from dotenv import load_dotenv
from lightrag import LightRAG
from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed
from lightrag.kg.shared_storage import initialize_pipeline_status
from lightrag.utils import setup_logger

# ロガーの設定
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

def get_rag():
    """Get initialized RAG instance."""
    return asyncio.run(initialize_rag())
