from collections import deque
import bisect
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = deque()
        for e in nums:
            if len(q) < k:
                bisect.insort(q, e)
            elif e > q[0]:
                q.popleft()
                bisect.insort(q, e)
        return q[0]