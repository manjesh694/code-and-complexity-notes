"""
NeetCode: Python for Coding Interviews
Topic: Sorting (3 / 5) - Sort Custom
URL: https://neetcode.io/problems/python-sort-custom/question

Problem Description:
-------------------
We can specify a custom sorting order by using the `key` parameter in Python's 
sorting methods (e.g., sorted() or .sort()). The `key` parameter accepts a function 
that returns a value to be used for sorting comparisons.

Challenge:
Implement the following two functions:

1. sort_words(words: List[str]) -> List[str]
   - Accepts a list of words.
   - Returns a NEW list of words sorted based on their length in DESCENDING order 
     (longest to shortest).

2. sort_numbers(numbers: List[int]) -> List[int]
   - Accepts a list of numbers.
   - Returns a NEW list of numbers sorted based on their absolute value in ASCENDING order 
     (smallest absolute value to largest).
   - Hint: Use the built-in abs() function.
"""

from typing import List


def sort_words(words: List[str]) -> List[str]:
    # Sorts based on string length, descending order
    return sorted(words, key=len, reverse=True)


def sort_numbers(numbers: List[int]) -> List[int]:
    # Sorts based on absolute value, ascending order
    return sorted(numbers, key=abs)


# ==========================================
# Test Cases / Verification
# ==========================================
if __name__ == "__main__":
    words_input = [
        "cherry",
        "apple",
        "blueberry",
        "banana",
        "watermelon",
        "zucchini",
        "kiwi",
        "pear",
    ]
    print("Sorted Words (by length, descending):")
    print(sort_words(words_input))

    numbers_input = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]
    print("\nSorted Numbers (by absolute value, ascending):")
    print(sort_numbers(numbers_input))