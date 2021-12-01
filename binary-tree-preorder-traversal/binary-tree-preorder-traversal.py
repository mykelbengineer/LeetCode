# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [(root, False)]
        
        while stack:
            
            node, visited = stack.pop()
            
            if node:
                
                if visited:
                    res.append(node.val)
                else:  
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))
                
        return res