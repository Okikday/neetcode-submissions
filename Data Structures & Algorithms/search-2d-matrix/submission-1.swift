class Solution {
    func searchMatrix(_ matrix: [[Int]], _ target: Int) -> Bool {
        let n = matrix[0].count
        var left = 0
        var right = (matrix.count * n) - 1 // (m * n) - 1
    
        while left <= right{
            let mid = left + (right - left) / 2
            let a = mid / n
            let b = mid % n
            if matrix[a][b] == target{
                return true
            }
            if matrix[a][b] < target{
                left = mid + 1
            }else{
                right = mid - 1
            }
        }
        return false
    }
}
