class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = 0
        for i in range(len(nums)):
            if nums[i] != n:
                return i
            n = n + 1
        
        return n
