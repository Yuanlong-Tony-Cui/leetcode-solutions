# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # NOTE:
        # - No need to use if-else when initializing depth_left since maxDepth(None) gives expected results.

        """
            Returns the num of nodes from current node to its furthest leaf node
        """

        if not root:
            return 0  # "0 nodes"
        
        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)
        return max(depth_left, depth_right) + 1
