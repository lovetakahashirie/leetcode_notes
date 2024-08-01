# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 難處：不能再左的定義
class Solution:
    def __init__(self):
        self.total = 0

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root.left==None and root.right==None:
            return 0 # 難1：如果只有root，return 0 而不是root.val。單純題目要求
        
        # 如果下面還有child，我就丟進去算數了
        self.sum2(root, fromLeft=False)
        return self.total

    def sum2(self, root, fromLeft: bool = False) -> None:
        # 難2：left leaf的定義：沒有child + 從左邊來
        if root.left==None and root.right==None and fromLeft==True:
            self.total += root.val
            return

        # 提醒：check了有再進去，保證進去不是none，避免麻煩
        if root.left:
            self.sum2(root.left, fromLeft=True)
        if root.right:
            self.sum2(root.right, fromLeft=False)
        return
