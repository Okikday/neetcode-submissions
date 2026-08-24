class Solution {
    func findMin(_ nums: [Int]) -> Int {
        var lo = 0
        var hi = nums.count - 1
        if nums[lo] < nums[hi]{
            return nums[lo]
        }
        while (hi - lo) > 1{
            let mid = (lo + hi) / 2
            if nums[lo] < nums[mid] && (nums[mid] < nums[lo] || nums[hi] < nums[lo]){
                lo = mid
            }else{
                hi = mid
            }
        }
        return min(nums[lo], nums[hi])
    }
}