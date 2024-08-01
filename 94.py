# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        output = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur) # 有就先記住你的route
                cur = cur.left # 再繼續走左
            else: # 1第一次探左路失敗 # 2第二次探右路失敗
                cur = stack.pop() # 1我回去上一部（中）
                # 2我也不需要回去上一個了，因爲第一次失敗已經放了中
                # 2我這個左subtree已經全部做完，我要再回去這整個subtree的上一層
                # 1我知道中已經是最左入的了，就把中放到output
                output.append(cur.val)
                # 1第一次探左路失敗，我現在要在下個loop進入右路
                cur = cur.right
        
        return output

# class Solution:
#     def __init__(self):
#         self.output = []
    
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root != None:
#             self.inorderTraversal(root.left)
#             self.output.append(root.val)
#             self.inorderTraversal(root.right)
#         return self.output
