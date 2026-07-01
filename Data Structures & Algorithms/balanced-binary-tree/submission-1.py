# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        #Calculate the height of each node
        def dfs(root):
            if not root:
                return 0
            
            return 1+max(dfs(root.left),dfs(root.right))

        dq=deque([root])
        while dq:
            node=dq.popleft()
            left=dfs(node.left)
            right=dfs(node.right)

            if(abs(left-right)>1):
                return False

            if(node.left):
                dq.append(node.left)
            if(node.right):
                dq.append(node.right)


        return True
        