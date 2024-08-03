# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n2)，因爲做n次，每次要pass len n list進去
# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
#         if not postorder:
#             return None
        
#         root = TreeNode(val = postorder[-1])

#         inIndex = inorder.index(root.val)

#         inL = inorder[:inIndex]
#         inR = inorder[inIndex+1:]

#         postL = postorder[:len(inL)]
#         postR = postorder[len(inL):-1]

#         root.left = self.buildTree(inL, postL)
#         root.right = self.buildTree(inR, postR)

#         return root

# O(n)，用hashmap代替list，只記住index就可以了，這樣就是constant
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inDict = {val: idx for idx, val in enumerate(inorder)}
        def build(start, end) -> List[int]:
            if start > end: # same as if not postorder
            # 但一定要大於，等於代表還有一個可以做
                return None
            
            rootVal = postorder.pop() # new list[-1] 就是右的中(看eg1)
            root = TreeNode(val = rootVal)
            rootIdx = inDict[rootVal]

            root.right = build(rootIdx+1, end)
            # 因爲我pop完后，[-1]是右的中，所以要先做右邊的
            # 我只要考慮start end of inorder list

            root.left = build(start, rootIdx-1)
            # 因爲recur的原理，我會先入right的全部，當我全部right做完，我就pop走了全部了，剩下的就自然是左的
            # 但要注意一點，這個仍然是切inorder的左part
            return root

        return build(0, len(inorder)-1)


        
