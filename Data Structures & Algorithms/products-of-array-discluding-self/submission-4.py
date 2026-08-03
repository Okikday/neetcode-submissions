class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        prefix_arr = [1]
        suffix_arr = [1]

        # prefix
        for i in range(1, num_len):
            diff = i - 1
            prefix_arr.append(prefix_arr[diff] * nums[diff])
            suffix_arr.append(suffix_arr[diff] * nums[num_len - i])
            
        len_diff = num_len - 1
        return [prefix_arr[i] * suffix_arr[len_diff - i] for i in range(num_len)]

