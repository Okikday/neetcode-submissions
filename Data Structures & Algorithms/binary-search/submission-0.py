class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search essentially

        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            mid_num = nums[mid]

            if mid_num == target:
                return mid
            elif mid_num < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return -1