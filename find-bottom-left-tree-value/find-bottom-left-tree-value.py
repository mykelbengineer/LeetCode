# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root: return []
        
        curr_level = [root]
        
        while curr_level:
            next_level = []

            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                    
                if node.right:
                    next_level.append(node.right)
                    
            if next_level:
                curr_level = next_level
            else:
                break
            
        return curr_level[0].val