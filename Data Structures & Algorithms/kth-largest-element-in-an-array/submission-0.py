from collections import deque
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = deque()

        for e in nums:
            if len(q) < k:
                self.binaryInsertion(q, e)
            elif e > q[0]:
                q.popleft()
                self.binaryInsertion(q, e)
        return q[0]

    
    def binaryInsertion(self, nums, val):
        l,r = 0, len(nums)

        while l < r:
            mid = l + (r-l) // 2
            if val > nums[mid]:
                l = mid + 1
            else:
                r = mid
        nums.insert(l, val)