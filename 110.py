# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 分成三部就可以
# if root==0，直接走
# if 該root的LR abs(depth difference)>1，直接走
# 該node沒問題，就問下面的兩個node
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        # 注意這個，是abs(差距)>1，不是差距>abs(1)，不然就沒了負數那邊
        if abs(self.findMaxDepth(root.left)-self.findMaxDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) & self.isBalanced(root.right)
        
    def findMaxDepth(self, root) -> int:
        if root==None:
            return 0
        return 1 + max(self.findMaxDepth(root.left), self.findMaxDepth(root.right))
