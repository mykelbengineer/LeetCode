# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        N = len(nums)
        
        if N == 0: return None
        
        def bst(nums, left, right):
            if left > right: return None
            
            mid = (left + right) // 2
            
            node = TreeNode(nums[mid])
            node.left = bst(nums, left, mid  - 1)
            node.right = bst(nums, mid + 1, right)
            
            return node
        
        return bst(nums, 0, N-1)