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
    func invertTree(_ root: TreeNode?) -> TreeNode? {
        guard let root = root else{return nil}
        // BFS
        var queue = Deque<TreeNode>()
        queue.prepend(root)

        while !queue.isEmpty{
            let node = queue.removeFirst()
            (node.left, node.right) = (node.right, node.left)

            if node.left != nil{queue.prepend(node.left!)}
            if node.right != nil{queue.prepend(node.right!)}
        }
        return root
    }
}
