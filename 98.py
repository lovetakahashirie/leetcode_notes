# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 用DFS inorder，只需要跟上一個人比較就可以
    def __init__(self):
        self.prev = None
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.isValidBST(root.left)
        # if self.prev and self.prev >= root.val: # 不要check value，因爲if self.prev，0和none都過不了，所以最好還是存node，就可以保證我只是check有沒有node，不會要考慮0
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        right = self.isValidBST(root.right)

        return left and right
