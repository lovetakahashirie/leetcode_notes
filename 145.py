# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def __init__(self):
#         self.output = []
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root != None:
#             self.postorderTraversal(root.left)
#             self.postorderTraversal(root.right)
#             self.output.append(root.val)
#         return self.output

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        stack = [root]
        output = []
        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return output[::-1]
