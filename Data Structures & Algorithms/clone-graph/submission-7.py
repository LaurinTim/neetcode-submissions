"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
                return None
        nodes = dict()

        def add_node(curr_node):
            if not curr_node:
                return None
                
            new_node = Node(val=curr_node.val, neighbors=[])
            nodes[curr_node] = new_node

            for neighbor in curr_node.neighbors:
                if neighbor in nodes:
                    new_node.neighbors.append(nodes[neighbor])
                else:
                    new_node.neighbors.append(add_node(neighbor))
            
            return new_node

        add_node(node)
        return nodes[node]
        