# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 難1：分case，當我
    # 難2：找到該key==root
    # 最後如果上面也做不了
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 這句是base case，到底就原裝回去什麽也不動
        if not root:
            return root

        # if cur node is the node that i want to delete
        if root.val == key:
            # 沒子，del自己
            if not root.left and not root.right:
                del root
                return None
            elif not root.left: # 不能寫elif root.left，root.left and root.right也會算進去
                right = root.right
                del root
                return right
            elif not root.right:
                left = root.left
                del root
                return left
            else:
                head, left = root.left, root.left
                right = root.right
                del root
                while left.right: # BST 特性，left.right.right....，接right
                    left = left.right
                left.right = right
                return head # 因爲left 移動了，所以要return 原本的left

        # 這個if else的目的是爲了接住下面，要麽接住更改完的head，要麽就接原裝
        if key < root.val:
            root.left = self.deleteNode(root.left, key) # 當下面是我的new root，丟給下面處理，處理好再接
        else:
            root.right =  self.deleteNode(root.right, key)

        # 這個一定要加上，這是最後兜底用的，上面已經做掉了root==none的case，到了這行，我就一定有root的
        return root


    
