"""Query RAG module."""

from lightrag import QueryParam
from lightrag_fefta.common import get_rag

def main():
    """Query RAG with different modes."""
    # Initialize RAG instance
    rag = get_rag()

    # クエリを実行
    query = "日本の首都について教えてください。"
    modes = ["naive", "local", "global", "hybrid", "mix"]

    for mode in modes:
        print(f"\nMode: {mode}")
        result = rag.query(query, param=QueryParam(mode=mode))
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
