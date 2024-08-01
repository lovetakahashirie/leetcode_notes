# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output = []
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root==None:
            return []
        self.findRoute(root=root)
        return self.output
        
    # 難1：到底的定義是LR都None，而不是其中一邊None，不然就會把拐彎前的那部分也當是了
    # 難2：因爲第一次進func我有check過root not None，而且進LR前也check過not None，所以每次進去就能直接加上我的cur val
    def findRoute(self, root, route = ""):
        if route == "":
            route = str(root.val)
        else:
            route += '->' + str(root.val)
        if root.left==None and root.right==None:
            self.output.append(route)
            return
        if root.left: self.findRoute(root.left, route)
        if root.right: self.findRoute(root.right, route)
        return
