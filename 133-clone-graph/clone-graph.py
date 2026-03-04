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

        if not node:
            return

        new_node = Node(val=node.val)

        deq = deque([node])
        map = {}
        map[node] = new_node


        while deq:

            for _ in range(len(deq)):
                curr_node = deq.popleft()

                for nbr in curr_node.neighbors:
                    if nbr not in map:
                        map[nbr] = Node(val=nbr.val) 
                        deq.append(nbr)

                    map[curr_node].neighbors.append(map[nbr])



        return new_node
