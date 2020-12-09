# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p,q)]
        
        while stack:
            node1, node2 = stack.pop()
            
            if not node1 and not node2:
                pass
            
            elif None in [node1, node2]:
                return False
            
            else:
                if node1.val != node2.val:
                    return False
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
        
        return True
                    
        
