# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val = val)
        if not root:
            return node
        if val > root.val:
            # BST search下去，不過要提前知道到底就指他
            if not root.right:
                root.right = node
            else:
                self.insertIntoBST(root.right, val)
        if val < root.val:
            if not root.left:
                root.left = node
            else:
                self.insertIntoBST(root.left, val)
        return root
