# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None
        
        curr = [root]
        output = []
        
        while curr:
            next_level = []
            level_nodes = []
            
            for node in curr:
                level_nodes.append(node.val)
                
                if node.left:
                    next_level.append(node.left)
                    
                
                if node.right:
                    next_level.append(node.right)
                    
            output.append(level_nodes[-1])
            curr = next_level
            
        
        return output
        