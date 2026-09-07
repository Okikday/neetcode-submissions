class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.rotatedSearch(nums, 0, len(nums)-1, target)

    def rotatedSearch(self, nums: List[int], l: int, r: int, target: int):
        if r-l == 0:
            if nums[r] == target:
                return r
            else:
                return -1
        if nums[l] > nums[r]:
            mid = l + (r-l)//2
            a = self.rotatedSearch(nums,l, mid, target)
            b = self.rotatedSearch(nums, mid+1, r, target)
            return max(a, b)
            
        if target > nums[r] or target < nums[l]:
            return -1
            
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return -1
