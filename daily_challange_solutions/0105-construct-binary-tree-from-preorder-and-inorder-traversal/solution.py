# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(pre,ino):
            if not ino:
                return None

            node=TreeNode(pre[0])
            idx=ino.index(pre[0])
            
            node.left=dfs(pre[1:1+idx],ino[:idx])
            node.right=dfs(pre[1+idx:],ino[idx+1:])
            
            return node
        
        return dfs(preorder,inorder)
