class Solution:
    def reverseBits(self, n: int) -> int:
        total = 0
        for i in range(32):
            total += (n & 1) * 2**(31-i)
            n = n >> 1
        return total
