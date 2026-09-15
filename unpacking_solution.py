"""
=============================================================================
TOPIC: Pythonic Code - Sequence Unpacking
PLATFORM: NeetCode (Python for Coding Interviews)
=============================================================================

PROBLEM DESCRIPTION / QUESTIONS:
--------------------------------
The goal of this exercise is to understand and apply sequence unpacking in 
Python to write cleaner and more readable code.

Challenge 1:
    Implement `sum_3_integers(triplet: List[int]) -> int`
    - Input: A list containing exactly 3 integers.
    - Output: The sum of the 3 integers using unpacking.

Challenge 2:
    Implement `compute_volume(box_dimensions: Tuple[int, int, int]) -> int`
    - Input: A tuple of 3 integers representing [width, height, depth] of a box.
    - Output: The volume of the box (width * height * depth) using unpacking.
=============================================================================
"""

from typing import List, Tuple

# =============================================================================
# SOLUTIONS
# =============================================================================


def sum_3_integers(triplet: List[int]) -> int:
    """Question 1: Takes a list of 3 integers and returns their sum using

    unpacking.
    """
    # Unpack the 3 elements directly into individual variables
    a, b, c = triplet

    return a + b + c


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    """Question 2: Takes a tuple of 3 integers representing

    (width, height, depth) and calculates the volume using unpacking.
    """
    # Unpack the tuple elements into descriptive variable names
    width, height, depth = box_dimensions

    return width * height * depth


# =============================================================================
# WHY I USED THESE POINTS (NOTES & INTERVIEW TAKEAWAYS)
# =============================================================================
"""
1. WHY UNPACKING OVER INDEXING?
   - Without unpacking:
         width = box_dimensions[0]
         height = box_dimensions[1]
         depth = box_dimensions[2]
   - With unpacking:
         width, height, depth = box_dimensions
   - Takeaway: Unpacking reduces 3 lines of code into 1, eliminates redundant
     array lookups, and avoids "magic index numbers" (0, 1, 2).

2. MEANINGFUL VARIABLE NAMES:
   - In `compute_volume`, variables are named `width, height, depth` rather 
     than `x, y, z`.
   - Takeaway: This makes the formula self-documenting and easy for anyone
     reviewing the code to understand the business logic immediately.

3. BUILT-IN SAFETY CHECK (ValueError):
   - Unpacking strictly enforces the length of the sequence:
       - Too few items  -> Raises `ValueError: not enough values to unpack`
       - Too many items -> Raises `ValueError: too many values to unpack`
   - Takeaway: It acts as an automatic assertion, preventing hidden bugs
     if unexpected inputs are passed.

4. COMPLEXITY:
   - Time Complexity:  O(1) (fixed 3 elements to unpack)
   - Space Complexity: O(1) (only 3 temporary variables created)
"""

# =============================================================================
# DRIVER CODE / TEST CASES (Do not modify)
# =============================================================================
if __name__ == "__main__":
    # Test cases for sum_3_integers
    print("--- Testing sum_3_integers ---")
    print(sum_3_integers([1, 2, 3]))  # Expected output: 6
    print(sum_3_integers([4, 6, 2]))  # Expected output: 12

    # Test cases for compute_volume
    print("\n--- Testing compute_volume ---")
    print(compute_volume((1, 2, 3)))  # Expected output: 6
    print(compute_volume((3, 2, 1)))  # Expected output: 6
    print(compute_volume((3, 9, 7)))  # Expected output: 189