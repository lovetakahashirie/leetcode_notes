# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 同類的問題：check same linked list, same string，想想就會發現思路是一樣的
# 不用print整個，就跟check same string一樣，同時做dfs，一有問題立刻return False
class Solution:
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

        
