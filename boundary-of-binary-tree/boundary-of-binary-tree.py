# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        def dfs_leftmost(node):
            if not node.left and not node.right:
                return 
            boundary.append(node.val)
            if node.left: dfs_leftmost(node.left)
            else: dfs_leftmost(node.right)
                
        
        def dfs_leaves(node):
            if not node.left and not node.right:
                boundary.append(node.val)
            if node.left: dfs_leaves(node.left)
            if node.right: dfs_leaves(node.right)
                
        
        def dfs_rightmost(node):
            if not node.left and not node.right:
                return
            if node.right: dfs_rightmost(node.right)
            else: dfs_rightmost(node.left)
            boundary.append(node.val)
            
        
        boundary = [root.val]
        
        if root.left:
            dfs_leftmost(root.left)
            dfs_leaves(root.left)
            
        if root.right:
            dfs_leaves(root.right)
            dfs_rightmost(root.right)
            
        return boundary