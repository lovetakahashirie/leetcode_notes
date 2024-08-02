# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 難1：要明白in pre post的構造
    # eg. inorder是 [左邊的nodes][中間的一個node][右邊的nodes]
    # 如果我想只要怎麽找出中間（才能切），我就需要pre/post，因爲中是靠邊的
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case：如果我用來找root的preorder list是empty，我只需要說這裏已經是none了
        if not preorder:
            return None
        
        # none處理了，把pre的第一個，也就是中做我們的root
        root = TreeNode(val = preorder[0])

        # 我知道中后，我就去inorder找index，再切割
        midIndex = inorder.index(root.val)
        leftInorder = inorder[:midIndex]
        rightInorder = inorder[midIndex+1:]

        # 切割完后，我也知道了左右，我可以切出下層要用的pre
        leftPreorder = preorder[1:len(leftInorder)+1]
        rightPreorder = preorder[len(leftInorder)+1:]

        # 然後我就去recur
        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)

        # 最後沒問題就return root給上一層
        return root
        
