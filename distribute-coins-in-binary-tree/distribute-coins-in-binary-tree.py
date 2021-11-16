# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.total_moves = 0
        
        def move_coins(node):
            if not node: return 0
            
            left = move_coins(node.left)
            right = move_coins(node.right)
            total_coins = left + right + node.val
            self.total_moves += abs(total_coins - 1)
            
            return total_coins - 1
        
        move_coins(root)
        
        return self.total_moves 
        