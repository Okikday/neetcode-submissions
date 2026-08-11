class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        cpy = list(set(nums))
        size = len(cpy)
        cpy.sort()
        
        
        i, count = 0, 1 if cpy else 0
        max_count = count

        while i+1 < size:
            if cpy[i] + 1 == cpy[i+1]:
                count += 1
            elif cpy[i] == cpy[i+1]:
                pass
            else:
                max_count = max(count, max_count)
                count = 1
            i += 1
            
        return max(count, max_count)

        
    def quickSort(self, nums: list[int], p: int, r: int) -> int:
        if p < r:
            q = self.partition(nums, p, r)
            self.quickSort(nums, p, q-1)
            self.quickSort(nums, q+1, r)
    
    def partition(self, nums: list[int], p, r) -> int:
        x = nums[r]
        i = p-1
        
        for j in range(p, r):
            if nums[j] <= x:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[r], nums[i+1] = nums[i+1], nums[r]
        return i+1

    def insertionSort(self, arr: list[int]):
        for j in range(1, len(arr)):
            key = arr[j]
            i = j - 1

            while i >= 0 and arr[i] > key:
                arr[i + 1] = arr[i]
                i -= 1

            arr[i + 1] = key


    

## Only for small numbers