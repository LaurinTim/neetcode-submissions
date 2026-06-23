class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            curr_node = self.cache[key]
            self.move_used_node(curr_node)
            return curr_node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            curr_node = self.cache[key]
            self.cache[key].val = value
            self.move_used_node(curr_node)
            return
        elif len(self.cache) == self.capacity:
            self.cache.pop(self.head.next.key, None)
            self.head.next.next.prev = self.head
            self.head.next = self.head.next.next

        new_node = Node(key, value)
        self.cache[key] = new_node
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        
    def move_used_node(self, curr_node):
        curr_node.prev.next = curr_node.next
        curr_node.next.prev = curr_node.prev
        curr_node.prev = self.tail.prev
        curr_node.next = self.tail
        self.tail.prev.next = curr_node
        self.tail.prev = curr_node
        
        
