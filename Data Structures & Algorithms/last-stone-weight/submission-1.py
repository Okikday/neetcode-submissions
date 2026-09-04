class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) <= 2:
            return abs(stones[0] - stones[1]) if len(stones) == 2 else stones[0]
        maxheap = stones
        heapq.heapify_max(maxheap)

        while len(maxheap) > 1:
            a = heapq.heappop_max(maxheap)
            b = heapq.heappop_max(maxheap)
            heapq.heappush_max(maxheap, abs(a-b))

        return maxheap[0]