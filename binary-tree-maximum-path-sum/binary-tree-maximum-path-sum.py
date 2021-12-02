# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.ans = float('-inf')
        
        def maxPath(node):
            
            if not node: return 0
            
            left = max(maxPath(node.left),0)
            right = max(maxPath(node.right),0)
            
            
            path = left + right + node.val
            
            self.ans = max(self.ans, path)
            
            return node.val + max(left, right)
            
            
        maxPath(root)
        
        return self.ans
            
            