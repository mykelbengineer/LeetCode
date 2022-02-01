# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        stack, comps = [root1], set()
        while stack: 
            node = stack.pop()
            comps.add(target - node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        stack = [root2]
        while stack:
            node = stack.pop()
            if node.val in comps:
                return True
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return False
            
                
            
                
            
            
            