# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        # 爲什麽max不用加（雖然加了也不會錯）這三句，是因爲max不需要考慮一邊none return0的情況，只看max就好，但如果是min，一邊是none，另一邊是有的，就會return了0但其實是錯的
        # if root.left == None:
        #     return 1 + self.maxDepth(root.right)
        # if root.right == None:
        #     return 1 + self.maxDepth(root.left)
            
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))