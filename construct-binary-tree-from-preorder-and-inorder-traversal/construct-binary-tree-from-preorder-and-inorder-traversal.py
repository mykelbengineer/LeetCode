# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return
        
        root = TreeNode(preorder[0])
        if len(preorder) == 1: return root
        
        i = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:i+1], inorder[:i+1])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        
        return root
        
        