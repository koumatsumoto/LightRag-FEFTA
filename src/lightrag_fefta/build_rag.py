"""Build RAG index module."""

from lightrag_fefta.common import get_rag


def main():
    """Build RAG index with sample documents."""
    # Initialize RAG instance
    rag = get_rag()

    # Read document from file
    with open("input_data/fefta_20240401.txt", "r", encoding="utf-8") as f:
        document = f.read()
        rag.insert(document)

    print("RAG index has been built successfully.")


if __name__ == "__main__":
    main()
