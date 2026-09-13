"""
=============================================================================
                              QUESTION
=============================================================================
Title: Sort Array by Parity (Segregate Even and Odd Numbers)

Problem Description:
-------------------
Given an array of integers `A`, write a function to reorder the array 
IN-PLACE so that all the EVEN integers appear at the beginning of the array, 
followed by all the ODD integers.

Note: The exact order within the even or odd groups does not matter.

Examples:
---------
Example 1:
    Input:  A = [3, 1, 2, 4]
    Output: [4, 2, 1, 3]  
    (Explanation: [2, 4, 3, 1] or [4, 2, 3, 1] are also acceptable)

Example 2:
    Input:  A = [0]
    Output: [0]

Example 3:
    Input:  A = [1, 3, 5, 2, 4]
    Output: [4, 2, 5, 1, 3]

Constraints:
------------
- Time Complexity:  O(N)
- Space Complexity: O(1) (Must be modified in-place)
=============================================================================
"""


# =============================================================================
#                               SOLUTION
# =============================================================================

def even_odd(A):
    """
    Rearranges the array in-place so evens come before odds 
    using the two-pointer technique.
    """
    next_even, next_odd = 0, len(A) - 1

    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            # Swap odd number to the back of the array
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

    return A


# =============================================================================
#                              TEST CASES
# =============================================================================

if __name__ == "__main__":
    test1 = [3, 1, 2, 4]
    print("Input 1: ", test1)
    even_odd(test1)
    print("Output 1:", test1)
    print("-" * 30)

    test2 = [1, 3, 5, 2, 4]
    print("Input 2: ", test2)
    even_odd(test2)
    print("Output 2:", test2)
    print("-" * 30)

    test3 = [0]
    print("Input 3: ", test3)
    even_odd(test3)
    print("Output 3:", test3)