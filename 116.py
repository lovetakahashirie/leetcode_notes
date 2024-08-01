"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# bfs, queue，一層一層做
# class Solution:
#     def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         if root == None:
#             return None

#         q = collections.deque()
#         q.append(root)

#         while q:
#             rightNode = None # 先重置rightnode，讓每行最右的都指向None
#             for _ in range(len(q)): # 該行有多少個node就要point幾次
#                 cur = q.popleft() # 最右而又未point的
#                 cur.next = rightNode # 指向右邊
#                 rightNode = cur # 你就是下個node的右邊

#                 # 我將自己處理完后，我要想下一層的次序
#                 if cur.right: # perfect check一個就好
#                     q.append(cur.right) # 把下一層的todo放進queue
#                     q.append(cur.left) # 先放右邊再放左邊
#         return root

# dfs, recursion
# class Solution:
#     def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         if root == None:
#             return None

#         # 總之我要先處理這三點
#         L, R, N = root.left, root.right, root.next
#         if L and R: # 我有下一層，我才要connect下一層的LR
#             L.next = R
#         if N and R: # 我有next and R，我才需要把R連過去Next的L
#             R.next = N.left
#         self.connect(L)
#         self.connect(R)
#         return root


# 也是bfs，但是用loop不用queue
# O(1) space
# 思路：想成一層層樓，電梯在最左邊，留個人在那邊，然後派另一個人去該層的每個node做一次
# 做完了，我們就去下一層，重複
class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        # 先記住頭
        head = root

        while root:
            cur = root

            while cur:
                L, R, N = cur.left, cur.right, cur.next
                if L and R:
                    L.next = R
                else:
                    break
                if R and N:  # 因爲perfect一定有
                    R.next = N.left
                cur = N

            root = root.left

        return head
