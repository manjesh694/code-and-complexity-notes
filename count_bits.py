"""
================================================================================
QUESTION:
================================================================================
Problem: Number of 1 Bits (Hamming Weight / Population Count)

Write a program to count the number of bits that are set to 1 in a non-negative 
integer. The program should test bits one-at-a-time starting with the 
least-significant bit, illustrating bit shifting and masking.

Example 1:
    Input:  12  (Binary: 1100)
    Output: 2

Example 2:
    Input:  15  (Binary: 1111)
    Output: 4
================================================================================
"""
# ans 


def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1  # 1. Masking
        x >>= 1  # 2. Right Shifting
    return num_bits


if __name__ == "__main__":
    # Test cases: (input, expected_output)
    test_cases = [
        (0, 0),  # 0b0      -> 0 bits
        (1, 1),  # 0b1      -> 1 bit
        (2, 1),  # 0b10     -> 1 bit
        (12, 2),  # 0b1100   -> 2 bits
        (15, 4),  # 0b1111   -> 4 bits
    ]

    for number, expected in test_cases:
        result = count_bits(number)
        assert result == expected, f"Failed on {number}: got {result}"
        print(f"Number: {number:<3} | Binary: {bin(number):>6} | 1s: {result}")

    print("\nAll tests passed successfully!")


"""
================================================================================
NOTES & INTERVIEW CONCEPTS
================================================================================

How it works (step-by-step):

1. Masking (x & 1):
   The bitwise AND operator & compares bits.
   Performing x & 1 checks the least significant bit (the rightmost bit). 
   If the last bit is 1, x & 1 evaluates to 1. 
   If it's 0, it evaluates to 0. 
   This is added to num_bits.

2. Right Shift (x >>= 1):
   Shifts all bits to the right by 1 position (equivalent to integer division by 2, dropping the remainder). 
   The bit we just checked is discarded, and the next bit moves into the rightmost position.

3. Condition (while x:):
   The loop continues until all bits are shifted away and x becomes 0.

Complexity:
   - Time Complexity: O(n), where n is the number of bits required to represent x (roughly log2(x)).
   - Space Complexity: O(1).

Key Python Details to Remember for Interviews:
   - Unbounded Integers: In Python 3, integers have no fixed size limit (unlike 32-bit or 64-bit limits in C/Java). 
     They can grow as large as your computer's RAM allows. You will never get an integer overflow error in Python.
   - sys.maxsize: Although Python integers can be infinitely large, sys.maxsize tells you the maximum integer 
     a standard pointer can address (typically 2**63 - 1 on modern 64-bit machines).
   - Floats are NOT unbounded: Unlike integers, floating-point numbers in Python do have limits (typically standard 64-bit double precision).
================================================================================
"""