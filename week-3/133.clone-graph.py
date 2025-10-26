"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # NOTE:
        # - For deep-clone tasks (e.g. a linked list, a graph), we use a dictionary to map old objects to their copies.

        if not node:
            return None

        old_to_new = {}
        def get_cloned_node(old_node: Node) -> Node:
            """
                Returns the cloned node.
                If the node is not cloned, this function clones it and returns the copy.
            """
            # Get
            if old_node in old_to_new:
                return old_to_new[old_node]

            # Clone
            copy = Node(old_node.val, [])
            old_to_new[old_node] = copy
            # Add the copies of its neighbours
            for neighbour in old_node.neighbors:
                copy.neighbors.append(get_cloned_node(neighbour))
            return copy

        return get_cloned_node(node)
