class Solution:
    def reverseBits(self, n: int) -> int:
        nums = [0] * 32
        for i in range(32):
            nums[i] = n & 1
            n = n >> 1
        return self.mul(nums)
    
    def mul(self, nums: List[int]) -> int:
        total = 0
        for i in range(31, -1, -1):
            total += nums[i] * 2**(31-i)
        return total
