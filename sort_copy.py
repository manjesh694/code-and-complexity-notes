"""
Sorted Copy

There is another way to sort a list in Python, using the sorted() function. 
The sorted() function returns a new list with the elements sorted in the specified order. 
The original list remains unchanged.

Examples:
1. Ascending order (default):
    words = ["kiwi", "pear", "apple", "banana", "cherry", "blueberry"]
    sorted_words = sorted(words)

2. Descending order (reverse=True):
    numbers = [5, -3, 2, -4, 6, -2, 4]
    sorted_numbers = sorted(numbers, reverse=True)

3. Custom key function:
    numbers = [5, -3, 2, -4, 6, -2, 4]
    sorted_numbers = sorted(numbers, key=abs)


Challenge Tasks:
1. sort_words(words: List[str]) -> List[str]
   - Accepts a list of words and returns a new list of words sorted in ASCENDING order.
   - Do NOT modify the original list.

2. sort_numbers(numbers: List[int]) -> List[int]
   - Accepts a list of numbers and returns a new list of numbers sorted in DESCENDING order 
     based on their absolute value.
   - Do NOT modify the original list.
"""

# ans

from typing import List


def sort_words(words: List[str]) -> List[str]:
    # Returns a new list of words sorted in ascending order
    return sorted(words)


def sort_numbers(numbers: List[int]) -> List[int]:
    # Returns a new list of numbers sorted by absolute value in descending order
    return sorted(numbers, key=abs, reverse=True)
# Test cases to see the output
words = ["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]
numbers = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]

print("--- Sorted Words (Ascending) ---")
print(sort_words(words))

print("\n--- Sorted Numbers (Descending by Absolute Value) ---")
print(sort_numbers(numbers))