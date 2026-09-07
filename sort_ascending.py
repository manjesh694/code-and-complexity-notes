"""
Problem: Sort Ascending
Platform: NeetCode (Python for Coding Interviews)
URL: https://neetcode.io/problems/python-sort-ascending/question

--- Description ---
In Python, you can sort a list of elements by calling `.sort()` on the list.
By default, the `.sort()` method sorts the elements in ascending order in-place.
The return value of the `.sort()` method is None.
This method also works for a list of strings (sorted in lexicographical order).

--- Challenge ---
Implement the following functions:
1. sort_words(words: List[str]) -> List[str]
   - Accepts a list of words and returns the list of words sorted in ascending order.

2. sort_numbers(numbers: List[int]) -> List[int]
   - Accepts a list of numbers and returns the list of numbers sorted in ascending order.

3. sort_decimals(numbers: List[float]) -> List[float]
   - Accepts a list of decimal numbers and returns the list of decimal numbers sorted in ascending order.

--- Complexity ---
- Time Complexity: O(n log n), where n is the number of elements in the list (uses Timsort).
- Space Complexity: O(n), where n is the number of elements in the list.
"""
# answer:
from typing import List


def sort_words(words: List[str]) -> List[str]:
    words.sort()
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort()
    return numbers


def sort_decimals(numbers: List[float]) -> List[float]:
    numbers.sort()
    return numbers


# --- Driver / Test Code ---
if __name__ == "__main__":
    print(
        sort_words(
            [
                "cherry",
                "apple",
                "blueberry",
                "banana",
                "watermelon",
                "zucchini",
                "kiwi",
                "pear",
            ]
        )
    )
    print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))
    print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))