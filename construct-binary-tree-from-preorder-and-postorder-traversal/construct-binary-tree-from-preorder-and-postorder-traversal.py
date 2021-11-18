# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not preorder: return
        root = TreeNode(preorder[0])
        preorder, postorder = preorder[1:], postorder[:-1]
        if not preorder: return root
        i = postorder.index(preorder[0])
        root.left = self.constructFromPrePost(preorder[:i+1], postorder[:i+1])
        root.right = self.constructFromPrePost(preorder[i+1:], postorder[i+1:])
        return root