# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 原理和104，111 find max min差不多，set了base case，直接用懶人方法recursive下去，1+L+R
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
