# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        head = root

        while head:
            if max(p.val, q.val) < head.val:
                head = head.left
            elif min(p.val, q.val) > head.val:
                head = head.right
            else:
                break
        
        return head