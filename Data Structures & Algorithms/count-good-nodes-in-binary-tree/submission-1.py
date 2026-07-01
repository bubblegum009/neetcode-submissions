# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        cmax=root.val
        def good(node,cmax):
            if not node:
                return 0
            if(node.val >= cmax):
                cmax=node.val
                return 1+good(node.left,cmax)+good(node.right,cmax)
            else:
                return good(node.left,cmax)+good(node.right,cmax)

        return good(root,cmax)