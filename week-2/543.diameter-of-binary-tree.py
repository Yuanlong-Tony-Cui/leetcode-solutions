# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # NOTE:
        # - At each node, there are two tasks: "getting the heights of the left and right node" and "getting the diameter through this node", but the function can only return a single value. Here we should return _the height_ since returning the diameter doesn't help knowing the diameter of its parent node. Instead of returning the diameter, we update it as a global variable.
        # - We let a None node (base case) have a height of -1, so that a leave node will have a height of 0.
        # NOTE (KEY): use `nonlocal` to make an outer variable globally read and changed by a function.

        diameter = 0

        def get_height(node: Optional[TreeNode]):
            """
                Gets the height of this node
            """
            nonlocal diameter  # NOTE: KEY
            if not node:
                return -1
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            diameter = max(diameter, left_height + right_height + 2)
            return max(left_height, right_height) + 1

        get_height(root)
        return diameter
