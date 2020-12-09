# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        self.res = []
        self.inOrder(root)
        
        return self.res == sorted(self.res) and len(set(self.res)) == len(self.res)
        
        
    def inOrder(self, root):
​
        if root is None:
            return
        
        else:
​
            self.inOrder(root.left)
            self.res.append(root.val)
            self.inOrder(root.right)
​
        
        
