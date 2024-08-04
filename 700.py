# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
# 很經典直接的題目，沒什麽好説的，一直做做到==位置就可以return，不然就是到底就return none
# 最後用none or root收尾，如果有root，none會被覆蓋掉
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        return self.searchBST(root.left, val) or self.searchBST(root.right, val)
