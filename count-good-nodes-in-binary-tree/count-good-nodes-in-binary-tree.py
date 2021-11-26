# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        
        max_so_far = float('-inf')
        curr = [(root, max_so_far)]
        num_of_good = 0
        
        while curr:
            
            node, direction_max = curr.pop()
                
            if direction_max <= node.val:
                num_of_good += 1

            if node.left:
                
                curr.append((node.left, max(direction_max, node.val)))

            if node.right:
                            
                curr.append((node.right, max(direction_max, node.val)))
            
        return num_of_good
        