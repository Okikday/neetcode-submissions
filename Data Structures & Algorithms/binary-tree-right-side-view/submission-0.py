# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def rec(root, h):
            if not root:
                return None
            if len(res) < h+1:
                res.append([])
            res[h].append(root.val)
            rec(root.left, h+1)
            rec(root.right, h+1)
        rec(root, 0)
        
        for i in range(len(res)):
            if res[i]:
                res[i] = res[i][-1]
            else:
                del res[i]
            
        return res