# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # NOTE:
        # - depth := dist from the root to a node
        # - height := dist from a node to its furthest leaf node
        # - Create a helper function that returns an `int` (more informative than `bool`) and use a "sentinel value" `float('-inf')` to indicate "unbalanced" --> This avoids redundant checking ("is it balanced?" plus "what is the height") at the same node.

        def get_height(node: TreeNode) -> int:
            """
                Gets the height of a given node
            """
            if not node:
                return -1  # base case

            # 3 unbalanced cases: left / right subtree is already unbalanced or height difference > 1
            left_height = get_height(node.left)
            if left_height == float('-inf'):
                return float('-inf')

            right_height = get_height(node.right)
            if right_height == float('-inf'):
                return float('-inf')

            if abs(left_height - right_height) > 1:
                return float('-inf')
            # float('-inf') propagates to its parent node

            return max(left_height, right_height) + 1
            
        return False if get_height(root) == float('-inf') else True
