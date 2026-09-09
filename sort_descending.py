"""
Problem: Sort Descending
Platform: NeetCode (Python for Coding Interviews)

Challenge:
Implement the following functions:

1. sort_words(words: List[str]) -> List[str]
   - Accepts a list of words and returns the list of words sorted in descending order.

2. sort_numbers(numbers: List[int]) -> List[int]
   - Accepts a list of numbers and returns the list of numbers sorted in descending order.

3. sort_decimals(numbers: List[float]) -> List[float]
   - Accepts a list of decimal numbers and returns the list of decimal numbers sorted in descending order.

Concept:
- The `.sort()` method accepts the `reverse` parameter (default is False).
- Passing `reverse=True` sorts the list in-place in descending order.
"""
# answers 

from typing import List


def sort_words(words: List[str]) -> List[str]:
    words.sort(reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(reverse=True)
    return numbers


def sort_decimals(numbers: List[float]) -> List[float]:
    numbers.sort(reverse=True)
    return numbers


# do not modify below this line
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