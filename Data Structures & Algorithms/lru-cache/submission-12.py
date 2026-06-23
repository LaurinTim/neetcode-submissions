class Node:
    def __init__(self, key=0, val=0, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.right = Node()
        self.left = Node()

        self.cache = {}
        
        self.right.prev, self.left.nxt = self.left, self.right

    def _insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev, node.nxt = prev, nxt
        prev.nxt, nxt.prev = node, node

    def _remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._insert(node)
        else:
            node = Node(key, value)
            self._insert(node)
            self.cache[key] = node

            if len(self.cache) > self.capacity:
                del self.cache[self.left.nxt.key]
                self._remove(self.left.nxt)
        
        
