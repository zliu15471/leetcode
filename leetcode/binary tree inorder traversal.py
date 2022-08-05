# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root,res):
            # Left -- Root -- Right
            if root:
                res = inorder(root.left,res)
                res.append(root.val)
                res = inorder(root.right,res)
            return res

        result = inorder(root, res)

        return result
