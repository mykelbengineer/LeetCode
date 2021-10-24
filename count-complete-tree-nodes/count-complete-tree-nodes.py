# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        cou = 0
        
        current = [root]
        
        while current:
            level_n = []
            next_l = []
            
            for node in current:
                level_n.append(node)
                
                if node.left:
                    next_l.append(node.left)
                    
                if node.right:
                    next_l.append(node.right)
                    
            cou += len(level_n)
            current = next_l
            
        
        return cou
        