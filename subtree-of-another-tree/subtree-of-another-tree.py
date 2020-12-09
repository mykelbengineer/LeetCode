# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
    
        def checkTree(root1, root2):
            if not root1 and not root2:
                return True
​
            elif root1 and not root2 or root2 and not root1:
                return False
​
            if root1.val != root2.val:
                return False
​
            return checkTree(root1.left, root2.left) and checkTree(root1.right, root2.right)
​
        def dfs(s,t):
            if not s:
                return False
​
            if s.val == t.val and checkTree(s, t):
                return True
​
            return dfs(s.left, t) or dfs(s.right, t)
    
        return dfs(s, t)
