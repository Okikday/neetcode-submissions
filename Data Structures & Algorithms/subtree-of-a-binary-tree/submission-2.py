# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if not(root1 or root2):
                return True
            if (root1 and root2 and root1.val == root2.val):
                return True and isEqual(root1.left, root2.left) and isEqual(root1.right, root2.right)
            return False
        
        # visited = set()
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            # if node not in visited:
                # visited.add(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if node.val == subRoot.val and isEqual(node, subRoot):
                return True
        
        return False
                
        
            


