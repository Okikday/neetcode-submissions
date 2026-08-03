class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        prefix_arr = [1 for i in range(num_len)]
        suffix_arr = [1 for i in range(num_len)]

        # prefix
        for i in range(1, num_len):
            prefix_arr[i] = prefix_arr[i - 1] * nums[i - 1]
        
        for i in range(num_len - 2, -1, -1):
            suffix_arr[i] = suffix_arr[i + 1] * nums[i + 1]
        
        return [prefix_arr[i] * suffix_arr[i] for i in range(num_len)]

