# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 難度在於拆case，先處理掉全部none的問題，然後就能放心做
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: # 所有node最後都是none，自然True
            return True
        if not root: # root none，自然False # both none的情況上面做了
            return False
        
        # 從這裏開始都不是none了，可能安心做
        if self.isSameTree(root, subRoot): # check這裏開始的兩個tree是否一樣，一樣就直接true
            return True

        # 這層不一樣的話就去下一層，任意一個true都可以
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # 直接把LC100的拿來用
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check base cases
        # False: X1, 1X, 23
        if (p and not q) or (not p and q) or (p and q and p.val!=q.val):
            return False

        # True: XX 到底了
        elif p==None and q==None:
            return True

        # 記得記得一定要處理完全部none p q再做這部，不然none是不能有L R的
        # 再觀望: 11 and 有下面
        else: # (p and q and p.val==q.val):
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
