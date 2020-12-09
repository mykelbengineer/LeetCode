# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        res = []
        flip = True
        current_level = [root]
        
        while current_level:
            level_nodes = []
            next_level = []
            flip ^= True
            
            for node in current_level:
                
                level_nodes.append(node.val)
                
                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)
                    
            
            if flip:
                res.append(level_nodes[::-1])
            else:
                res.append(level_nodes)
            
            current_level = next_level
        
        return res
        
