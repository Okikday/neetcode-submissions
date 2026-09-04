from collections import deque
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.filled = False
        self.k = k
        nums.sort()
        self.q = deque(nums[-k:]) if len(nums) > k  else deque(nums)

        if len(self.q) == self.k:
            self.filled = True

    def add(self, val: int) -> int:
        if not self.filled:
            self.binaryInsertion(self.q, val)
            if len(self.q) == self.k:
                self.filled = True
        elif val > self.q[0]:
            self.q.popleft()
            self.binaryInsertion(self.q, val)
        return self.q[0]

    def binaryInsertion(self, nums, val):
        l = 0 # left
        r = len(nums) # right

        while l < r:
            mid = l + (r - l) // 2
            if val > nums[mid]:
                l = mid + 1
            else:
                r = mid
            
        nums.insert(l, val)