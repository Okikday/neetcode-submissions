class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found_map = {}

        for i in range(0, len(nums)):
            find = target - nums[i]
            if find in found_map:
                return [found_map[find], i]
            found_map[nums[i]] = i

        return []