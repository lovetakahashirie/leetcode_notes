# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def __init__(self):
#         self.output = []
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root!=None:
#             self.output.append(root.val)
#             self.preorderTraversal(root.left)
#             self.preorderTraversal(root.right)

#         return self.output

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        output = []
        todo = [root]
        while todo: # 代表我還有node未加到output
            node = todo.pop()
            output.append(node.val)
            
            # look at my next todo
            if node.right:
                todo.append(node.right)
            if node.left:
                todo.append(node.left)


        return output
