"""
File Operations Package
=======================
This module handles basic file read/write operations.
"""

def write_to_file(filename: str, content: str) -> None:
    """Write content to a file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def read_from_file(filename: str) -> str:
    """Read content from a file."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()
