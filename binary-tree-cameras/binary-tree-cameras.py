# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if node is None:
                return 'covered'
            l, r = dfs(node.left), dfs(node.right)
            if l==r=='covered':
                return 'to_be_covered'
            if l=='to_be_covered' or r=='to_be_covered':
                self.res += 1
                return 'covering'
            if l=='covering' or r=='covering':
                return 'covered'
        return (dfs(root)=='to_be_covered') + self.res
        