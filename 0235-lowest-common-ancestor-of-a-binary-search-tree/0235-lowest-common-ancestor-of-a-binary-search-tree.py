# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        while root:
            # go left
            if p.val < root.val and q.val < root.val:
                root = root.left
            
            # go right
            elif p.val > root.val and q.val > root.val:
                root = root.right
            
            # split point → LCA found
            else:
                return root
        