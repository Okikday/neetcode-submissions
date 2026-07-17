class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_map: dict[int] = {}

        
        for num in nums:
            nums_map[num] = nums_map.get(num, 0) + 1

        return sorted(nums_map.keys(), key=lambda x: nums_map[x], reverse=True)[:k]

