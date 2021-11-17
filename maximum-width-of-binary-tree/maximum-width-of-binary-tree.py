# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        current =[(root, 0)]
        
        while current:
            ans = max(ans, current[-1][1] - current[0][1] + 1)
            next_level = []
            
            for node, pos in current:
                if node.left:
                    next_level.append((node.left, pos * 2))
                    
                if node.right:
                    next_level.append((node.right, pos * 2 + 1))

            
            current = next_level
            
        
        return ans
            
        