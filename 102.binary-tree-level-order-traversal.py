# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # NOTE:
        # - The trick here is to use an embedded loop, so that we won't move to the next iteration (next level) until all nodes at the current level are consumed.

        if not root:
            return []

        queue = deque([root])  # always stores nodes by level
        res = []
        while queue:  # while the next level exists
            lvl_size = len(queue)
            lvl = []  # stores node values for this level
            for i in range(lvl_size):
                node = queue.popleft()
                lvl.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # At this point, all nodes at this level has been consumed
            res.append(lvl)

        return res
