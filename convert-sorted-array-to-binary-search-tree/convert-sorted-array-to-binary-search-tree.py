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
        
        def BST(nums, left, right):
            if left > right: return None
            
            mid = (left + right) // 2
            
            root = TreeNode(nums[mid])
            root.left = BST(nums,left, mid-1)
            root.right = BST(nums, mid+1, right)
            
            return root
        
        return BST(nums, 0, N-1)
        