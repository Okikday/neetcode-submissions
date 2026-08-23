class Solution {
    func searchMatrix(_ matrix: [[Int]], _ target: Int) -> Bool {
        let m = matrix.count
        let n = matrix[0].count
        var r = 0, c = n - 1

        while r < m && c >= 0 {
            if matrix[r][c] > target {
                c -= 1
            } else if matrix[r][c] < target {
                r += 1
            } else {
                return true
            }
        }
        return false
    }
}