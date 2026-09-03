from collections import deque
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.filled = False
        self.k = k
        nums.sort()
        nums_len = len(nums)
        if nums_len > k:
            self.q = deque(nums[nums_len - k:])
            self.rest = nums[0: nums_len - k]
        else:
            self.q = deque(nums)
            self.rest = list()
        
        if len(self.q) == self.k:
            self.filled = True

    def add(self, val: int) -> int:
        if not self.filled:
            self.binaryInsertion(self.q, val)
            if len(self.q) == self.k:
                self.filled = True
            return self.q[0]
        if val > self.q[0]:
            self.binaryInsertion(self.rest, self.q.popleft())
            self.binaryInsertion(self.q, val)
        else:
            self.binaryInsertion(self.rest, val)
        print(self.q, self.rest)
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

