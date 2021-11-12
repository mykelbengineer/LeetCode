# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, left, right, array):
        if left > right:
            return None
        
        mid = left + (right - left) // 2
        root = TreeNode(array[mid])
        root.left = self.helper(left, mid - 1, array)
        root.right = self.helper(mid + 1, right, array)
        return root
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(0, len(nums) - 1, nums)
        
        
    
        