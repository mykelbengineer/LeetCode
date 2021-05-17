# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums:
            max_value_index, max_value = max(enumerate(nums), key=lambda x:x[1])
            node = TreeNode(max_value)
            node.left = self.constructMaximumBinaryTree(nums[:max_value_index])
            node.right = self.constructMaximumBinaryTree(nums[max_value_index+1:])
        
            return node
        
        