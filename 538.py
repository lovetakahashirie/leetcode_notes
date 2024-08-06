# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.bigger = 0

    # 從右邊開始，沒做完一個，自己+更右邊的就一定比左邊下一個大，然後一直叠加過去就可以
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        self.convertBST(root.right)
        self.bigger += root.val
        root.val = self.bigger
        self.convertBST(root.left)
        return root
