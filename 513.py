# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 其實很簡單，就是BFS的變種，直接開個node，每去新一層就拿queue的第一個就好
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])
        botLeft = None
        while q:
            botLeft = q[0]
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
        return botLeft.val

