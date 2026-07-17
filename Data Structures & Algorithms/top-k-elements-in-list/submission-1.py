class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_map: dict[int] = {}

        
        for num in nums:
            nums_map[num] = nums_map.get(num, 0) + 1

        return heapq.nlargest(k, nums_map.keys(), key=nums_map.get)

