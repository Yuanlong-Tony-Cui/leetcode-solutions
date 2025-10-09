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
        # - Create a helper function that returns an `int` (more informative than `bool`) and use a special number -1 to indicate "unbalanced" --> This avoids redundant checking ("is it balanced?" plus "what is the height") at the same node.
        # - Introduce a customized concept of "index" since height DNE on a None node.

        def get_index(node: TreeNode) -> int:
            """
                Gets the index of a given node (index := height + 1) (index := 0 for None nodes)
                (NOTE: A leaf node has a height of 0 but an "index" of 1. It is defined as such, so that a None node, whose height is undefined, can have an "index" of 0.)
                Returns:
                    the "index" if this node is height-balanced;
                    -1 if this node is not height-balanced.
            """
            if not node:
                return 0  # base case

            # 3 unbalanced cases: left / right subtree is already unbalanced or height difference > 1
            left_node_index = get_index(node.left)
            if left_node_index == -1:
                return -1

            right_node_index = get_index(node.right)
            if right_node_index == -1:
                return -1

            if abs(left_node_index - right_node_index) > 1:
                return -1
            # -1 propagates to its parent node
                
            return max(left_node_index, right_node_index) + 1
            
        return False if get_index(root) == -1 else True
