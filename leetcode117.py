"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# 其實和LC116的原理一樣，不過不能直接next過去，要按照順序去試
# 以L找next爲例，if R then R, elif while next then next.R, next.L, next.next.L, .R一直試完，同層全部都沒有才算沒有next
# 另一個考核點是find next root，要用marker記住第一個找到的下一層的node，這就是下一層的root
# 有考慮到這兩個后，用if else慢慢寫就可以了
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        head = root
        while root:
            cur = root
            nextLoopRoot = None
            gotRoot = False
            while cur:
                L, R, N = cur.left, cur.right, cur.next
                if L:
                    if gotRoot == False:
                        nextLoopRoot = L
                        gotRoot = True
                    if R:
                        L.next = R
                    else:
                        while N:
                            if N.left:
                                L.next = N.left
                                break
                            elif N and N.right:
                                L.next = N.right
                                break
                            N = N.next
                if R:
                    if gotRoot == False:
                        nextLoopRoot = R
                        gotRoot = True
                    while N:
                        if N.left:
                            R.next = N.left
                            break
                        elif N.right:
                            R.next = N.right
                            break
                        N = N.next
                cur = cur.next
            root = nextLoopRoot
        return head