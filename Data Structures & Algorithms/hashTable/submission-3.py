class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}


    def insert(self, key: int, value: int) -> None:
        if key in self.hash_map.keys():
            self.hash_map[key] = value
        else:
            if self.getSize() + 1 >= self.capacity/2:
                self.resize()
            self.hash_map[key] = value


    def get(self, key: int) -> int:
        return self.hash_map.get(key, -1)


    def remove(self, key: int) -> bool:
        return self.hash_map.pop(key, None) is not None


    def getSize(self) -> int:
        return len(self.hash_map)


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        self.capacity *= 2

