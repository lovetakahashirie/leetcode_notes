# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []:
            return None
        mid = len(nums)//2 # 自動floor了
        root = TreeNode(val = nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid]) # mid-1就是最後要的index
        root.right = self.sortedArrayToBST(nums[mid+1:]) # 因爲mid用來開node了，所以要從下個index開始
        return root
