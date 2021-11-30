# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return None
        
        output = []
        final = []
        path = [root.val]
        stack = [(root, path)]
        
        while stack:
            
            node, pathSums = stack.pop()
            
            if not node.left and not node.right:
                output.append(pathSums)
                
            if node.left:
                stack.append((node.left, pathSums + [node.left.val]))
                
            if node.right:
                stack.append((node.right, pathSums + [node.right.val]))
                
        
        for pat in output:
            if sum(pat) == targetSum:
                final.append(pat)
                
                
        return final
                
            
        