class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.len = 0
        self.arr = [None]*self.capacity
        self.last_entry_pos = -1


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        if self.arr[i] is None:
            self.len += 1
            if i > self.last_entry_pos:
                self.last_entry_pos = i
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.len == self.capacity:
            self.resize()
        self.last_entry_pos += 1
        if self.arr[self.last_entry_pos] is None:
            self.len += 1
        self.arr[self.last_entry_pos] = n


    def popback(self) -> int:
        popped_entry = self.arr[self.last_entry_pos]
        self.arr[self.last_entry_pos] = None
        self.len -= 1
        self.last_entry_pos = max(0, self.last_entry_pos - 1)
        return popped_entry
 

    def resize(self) -> None:
        self.arr += [None] * self.capacity
        self.capacity *= 2


    def getSize(self) -> int:
        return self.len
        
    
    def getCapacity(self) -> int:
        return self.capacity
