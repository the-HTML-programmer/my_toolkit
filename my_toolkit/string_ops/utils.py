"""
String Operations Package
=========================
This module contains string manipulation functions.
"""

def reverse_string(s: str) -> str:
    """Return the reversed version of a string."""
    return s[::-1]

def count_vowels(s: str) -> int:
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
