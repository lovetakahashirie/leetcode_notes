# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # 先寫base
        if root == None:
            return None
        # if cur < low，我還要考慮cur.right，因爲是>cur 但不一定<low，只是<上一手
        if root.val < low:
            head = root.right # 先設定好要下一輪的東西
            root.right = None # 斷開，架空整個subtree
            self.delTree(root) # 將整個subtree del
            return self.trimBST(head, low, high) # 把新root丟給下一手處理 # 這裏需要特別主力
        elif root.val > high:
            head = root.left
            root.left = None
            self.delTree(root)
            return self.trimBST(head, low, high)
        root.left = self.trimBST(root.left, low, high) # 再想好下一層要怎麽接
        root.right = self.trimBST(root.right, low, high)
        return root # 最後return 沒動過的root
    def delTree(self, root) -> None:
        if not root:
            return
        self.delTree(root.left)
        self.delTree(root.right)
        del root
        return
