# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        # 這2句很重要，如果一邊none，我們不能只return0，要再看另一邊
        # 但如果是max就不用，因爲max根本不會考慮0
        if root.left == None:
            return 1 + self.minDepth(root.right)
        if root.right == None:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
