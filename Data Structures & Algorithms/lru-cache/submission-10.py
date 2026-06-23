class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key, self.val = key, val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.right = Node()
        self.left = Node()
        self.left.next = self.right
        self.right.prev = self.left

    
    def _insert(self, node):
        prev, next = self.right.prev, self.right
        node.prev, node.next = prev, next
        prev.next, next.prev = node, node

    
    def _remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        

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
                del self.cache[self.left.next.key]
                self._remove(self.left.next)
        
