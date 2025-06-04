# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.summ=0
        def dfs(node):
            if not node:
                return
            if low<= node.val <= high:
                self.summ+=node.val
            if node.val<=high:
                dfs(node.right)
            if node.val>=low:
                dfs(node.left)
            return 
        dfs(root)
        return self.summ

