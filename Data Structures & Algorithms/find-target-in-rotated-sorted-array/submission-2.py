class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def rotatedSearch(l: int, r: int):
            if r-l == 0:
                return r if nums[r] == target else -1
            if nums[l] > nums[r]:
                m = l + (r-l)//2
                return max(rotatedSearch(l, m), rotatedSearch(m+1, r))
                
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

        return rotatedSearch(0, len(nums)-1)


