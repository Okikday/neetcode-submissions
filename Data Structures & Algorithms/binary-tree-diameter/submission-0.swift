/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     var val: Int
 *     var left: TreeNode?
 *     var right: TreeNode?
 *     init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */

class Solution {
    func diameterOfBinaryTree(_ root: TreeNode?) -> Int {
        var count = 0

        func dfs(_ root: TreeNode?) -> Int{
            guard let root = root else{return 0}
            let l = dfs(root.left)
            let r = dfs(root.right)
            count = max(count, l + r)
            return 1 + max(l, r)
        }
        dfs(root)
        return count
    }
}