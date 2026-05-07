class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    
    def _hash(self, key: int):
        return key % self.capacity


    def insert(self, key: int, value: int) -> None:
        index = self._hash(key)
        
        if self.table[index] is None:
            self.size += 1
            self.table[index] = Node(key, value)
            if (self.size) / self.capacity >= 0.5:
                self.resize()
            return
        
        curr = self.table[index]
        while curr:
            if curr.key == key:
                curr.value = value
                return
            if curr.next is None:
                break
            curr = curr.next
        
        self.size += 1
        curr.next = Node(key, value)

        if (self.size) / self.capacity >= 0.5:
            self.resize()


    def get(self, key: int) -> int:
        index = self._hash(key)

        if self.table[index] is None:
            return -1
        
        curr = self.table[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        
        return -1


    def remove(self, key: int) -> bool:
        index = self._hash(key)
        curr = self.table[index]
        prev = None
        
        while curr:
            if curr.key == key:
                if prev is None:
                    self.table[index] = curr.next
                else:
                    prev.next = curr.next
                
                self.size -= 1
                return True
                
            prev = curr
            curr = curr.next
            
        return False


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        old_table = self.table
        self.capacity *= 2
        self.size = 0
        self.table = [None] * self.capacity

        for node in old_table:
            curr = node
            while curr:
                self.insert(curr.key, curr.value)
                curr = curr.next

