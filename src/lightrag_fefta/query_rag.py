"""Query RAG module."""

import argparse
from typing import Literal

from lightrag import QueryParam
from lightrag_fefta.common import get_rag

RAGMode = Literal["naive", "local", "global", "hybrid", "mix"]
VALID_MODES: list[RAGMode] = ["naive", "local", "global", "hybrid", "mix"]


def validate_query(query: str) -> str:
    """Validate query string."""
    if not query or len(query.strip()) == 0:
        raise argparse.ArgumentTypeError("Query must not be empty")
    return query.strip()


def validate_mode(mode: str) -> RAGMode:
    """Validate RAG mode."""
    if mode not in VALID_MODES:
        raise ValueError(f"Invalid mode: {mode}. Must be one of {VALID_MODES}")
    return mode


def get_args() -> argparse.Namespace:
    """Get command line arguments."""
    parser = argparse.ArgumentParser(description="Query RAG system")
    parser.add_argument(
        "query",
        type=validate_query,
        help="Query text (must not be empty)",
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=VALID_MODES,
        default="mix",
        help="RAG mode (default: mix)",
    )
    return parser.parse_args()


def main():
    """Query RAG with specified mode."""
    args = get_args()

    # Initialize RAG instance
    rag = get_rag()

    # Validate mode
    mode = validate_mode(args.mode)

    # Execute query
    result = rag.query(args.query, param=QueryParam(mode=mode))
    print(f"\nMode: {mode}")
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
