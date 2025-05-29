# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.v=0
        def dfs(node,curmax,curmin):
            if not node:
                return None

            
            if node.val>curmax:
                curmax=node.val
            if node.val<curmin:
                curmin=node.val
            self.v=max(self.v,abs(curmax-curmin))
            dfs(node.left,curmax,curmin)
            dfs(node.right,curmax,curmin)
            
        dfs(root,root.val,root.val)
        return self.v
        
