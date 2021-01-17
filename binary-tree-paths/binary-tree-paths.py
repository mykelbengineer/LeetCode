# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        
        res = [] 
        stack = [('', root)]
        
        while stack:
            ls, node = stack.pop()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            
            if node.left:
                stack.append((ls + str(node.val) + '->', node.left))
                
            if node.right:
                stack.append((ls + str(node.val) + '->', node.right))
                
        return res
            
                
