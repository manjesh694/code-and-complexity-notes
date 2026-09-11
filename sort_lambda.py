"""
Challenge: Sort Lambda
Platform: NeetCode (Python for Coding Interviews)

Description:
Defining a separate function just to pass it into the `key` parameter of the `.sort()`
method or `sorted()` function can be cumbersome. We can use a `lambda function` to 
define a function in a single line and pass it directly.

Syntax:
    lambda <parameter>: <expression>

Challenge Tasks:
1. sort_words(words: List[str]) -> List[str]
   - Accepts a list of words and returns a new list of words sorted based on 
     their length in DESCENDING order.
   - Use a lambda function to sort the words by their length.

2. sort_numbers(numbers: List[int]) -> List[int]
   - Accepts a list of numbers and returns a new list of numbers sorted based on 
     their absolute value in ASCENDING order.
   - Use a lambda function to sort the numbers by their absolute value.
"""
# ans 

from typing import List


def sort_words(words: List[str]) -> List[str]:
    # Sorts words by length in descending order
    return sorted(words, key=lambda word: len(word), reverse=True)


def sort_numbers(numbers: List[int]) -> List[int]:
    # Sorts numbers by their absolute value in ascending order
    return sorted(numbers, key=lambda num: abs(num))


# Test cases
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

    print(
        sort_numbers(
            [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]
        )
    )