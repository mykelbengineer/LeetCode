# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, output):
        if node:
            if node.left or node.right:
                self.dfs(node.left, output) or self.dfs(node.right, output)
            
            output.append(node.val)
    
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        self.dfs(root, output)

        return output