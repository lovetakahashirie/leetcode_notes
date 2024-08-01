# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: # eg3
            return []
         
        output = []

        def f(cur, lv): 
            if cur == None:
                return
            if len(output) < lv: # 星星：lv不一定要用counter，可以直接用len
                output.append([])
            output[lv-1].append(cur.val)
            f(cur.left, lv+1)
            f(cur.right, lv+1)
        
        f(root, lv=1)
        output2 = []
        for lv in output:
            output2.append(max(lv))
        return output2