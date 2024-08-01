# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 難在如何分case，10，01，11，00，只有這4種可能
        if root.right==None and root.left==None:
            return True
        else:
            # 當你確認可以compare時，就丟給compare的func
            return self.compare(root.right, root.left)

    def compare(self, L: Optional[TreeNode], R: Optional[TreeNode]) -> bool:
        # 同樣也是分case
        if R==None and L==None:
            return True
        elif R and L and R.val==L.val: # 但這裏除了有node外，還要check val
            # 然後我就丟給下一輪處理了，一直對稱爆開
            return self.compare(L.left, R.right) & self.compare(L.right, R.left)
        else:
            return False
