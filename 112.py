# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # dfs本身沒錯，但是不一定要從上到下，我們可以用剩下的target解決
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 先處理誤入none的情況，直接false
        if not root:
            return False
        
        # 如果到底了，就check剩下的是不是
        if not root.left and not root.right:
            return targetSum == root.val
        
        # 上面已經清掉了none cases，現在recur下去問LR ==
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
