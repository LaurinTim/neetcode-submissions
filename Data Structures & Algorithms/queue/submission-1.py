class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        new_node = Node(value)
        self.tail.prev.next = new_node
        new_node.prev = self.tail.prev
        self.tail.prev = new_node
        new_node.next = self.tail
        

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        popped_value = self.tail.prev.value
        new_last_node = self.tail.prev.prev
        new_last_node.next = self.tail
        self.tail.prev = new_last_node
        return popped_value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        popped_value = self.head.next.value
        new_first_node = self.head.next.next
        new_first_node.prev = self.head
        self.head.next = new_first_node
        return popped_value
        
