class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = stones
        heapq.heapify_max(maxheap)

        while len(maxheap) > 1:
            a = heapq.heappop_max(maxheap)
            b = heapq.heappop_max(maxheap)
            heapq.heappush_max(maxheap, abs(a-b))

        return maxheap[0]