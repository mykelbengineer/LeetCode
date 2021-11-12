# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        self.dfs(root, res)
        
        return res
        
    def dfs(self, root, output):
        
        if root:
            output.append(root.val)
            
            self.dfs(root.left, output)
            self.dfs(root.right, output)
            