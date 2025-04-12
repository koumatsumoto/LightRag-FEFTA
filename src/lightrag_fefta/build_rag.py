"""Build RAG index module."""

from lightrag_fefta.common import get_rag


def main():
    """Build RAG index with sample documents."""
    # Initialize RAG instance
    rag = get_rag()

    # サンプルドキュメントを追加
    documents = [
        "東京は日本の首都です。",
        "富士山は日本一高い山です。",
        "京都には多くの寺社仏閣があります。",
    ]
    for doc in documents:
        rag.insert(doc)

    print("RAG index has been built successfully.")


if __name__ == "__main__":
    main()
