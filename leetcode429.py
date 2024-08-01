"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 開始前先搞清楚，binary tree是left，right
# 但n-ary tree是給你一個child list，你要for loop 去access各個child node
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []

        def f(cur, lv):
            if cur == None:
                return
            if len(output) < lv:
                output.append([])
            output[lv-1].append(cur.val)
            
            for child in cur.children:
                f(child, lv+1)

        output = []
        f(root, lv=1)

        return output
