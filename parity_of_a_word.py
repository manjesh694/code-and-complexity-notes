# parity.py

# ---------- Solution 1: Brute Force ----------
def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


# ---------- Solution 2: Erase the Lowest Set Bit ----------
def parity_fast(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1   # Drops the lowest set bit of x
    return result


# ---------- Solution 3: Lookup Table ----------
MASK_SIZE = 16
BIT_MASK = 0xFFFF

# Precompute parity for every possible 16-bit value (0 to 65535)
PRECOMPUTED_PARITY = [parity(i) for i in range(1 << MASK_SIZE)]

def parity_lookup(x):
    return (PRECOMPUTED_PARITY[(x >> (3 * MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^
            PRECOMPUTED_PARITY[x & BIT_MASK])


# ---------- Test ----------
if __name__ == "__main__":
    test_value = 13  # 1101 in binary -> three 1s -> odd -> parity 1
    print("Brute force:          ", parity(test_value))
    print("Fast (drop lowest bit):", parity_fast(test_value))
    print("Lookup table:         ", parity_lookup(test_value))


# ==============================================================================
# NOTES & EXPLANATION important 
# ==============================================================================
"""
Solution 1 (Brute Force):
-------------------------
- x & 1: grabs the last bit of x.
- result ^= (that bit): flips result each time a 1-bit is seen — since XOR-ing 
  with 1 toggles a bit, and XOR-ing with 0 leaves it unchanged, result ends up 
  holding the parity.
- x >>= 1: shifts x right to look at the next bit.
- Time complexity: O(n) — where n is the total number of bits (e.g., 64), 
  because it checks every bit, even the 0s.

Solution 2 (Erase Lowest Set Bit):
----------------------------------
- x & (x - 1): clears/drops the lowest set bit of x.
- Skips all 0s and only loops as many times as there are 1s.
- Time complexity: O(k) — where k is the number of bits set to 1.

Solution 3 (Lookup Table):
--------------------------
- Instead of caching all 2^64 values (impossible in memory), we cache 16-bit 
  chunks (2^16 = 65,536 entries).
- Breaks 64-bit integer into four 16-bit words, looks up each, and XORs them.
- Time complexity: O(1) per query — best when doing millions of lookups.
"""