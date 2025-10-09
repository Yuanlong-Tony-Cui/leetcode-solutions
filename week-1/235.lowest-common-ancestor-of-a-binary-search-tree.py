# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # NOTE:
        # - Key observation: the LCA node must have p and q _separate_ in its left and right subtrees, _and_ for BSTs, we know which subtree has the target node by comparing its value with the current node's value.
        # - When calling a recursive function, double check if we need to use `return` to pass its returned value to its caller!

        smaller_val = min(p.val, q.val)
        larger_val = max(p.val, q.val)
        if root.val == smaller_val or root.val == larger_val:  # special case (Example 2)
            return root
        else:  # root, p, and q have distinct values
            if smaller_val < root.val and root.val < larger_val:  # typical case
                return root
            elif smaller_val < root.val and larger_val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else: # root.val < smaller_val and root.val < larger_val
                return self.lowestCommonAncestor(root.right, p, q)
        
        # All cases covered. No return needed here.
