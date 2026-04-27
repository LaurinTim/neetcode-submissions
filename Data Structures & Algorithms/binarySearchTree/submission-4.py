class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None
        self.key_map = {}


    def insert(self, key: int, val: int) -> None:
        new_node = Node(key, val)
        curr_node = self.root
        if curr_node is None:
            self.root = new_node
            curr_node = self.root

        while curr_node.key != key:
            if curr_node.key > key:
                if curr_node.left is None:
                    curr_node.left = new_node
                curr_node = curr_node.left
            elif curr_node.key < key:
                if curr_node.right is None:
                    curr_node.right = new_node
                curr_node = curr_node.right
        
        self.key_map[key] = val
        self.key_map = dict(sorted(self.key_map.items()))
        print(key, val, list(self.key_map.items()))


    def get(self, key: int) -> int:
        return self.key_map.get(key, -1)


    def getMin(self) -> int:
        if self.root is None:
            return -1
        return next(iter(self.key_map.values()))


    def getMax(self) -> int:
        if self.root is None:
            return -1
        return next(reversed(self.key_map.values()))


    def remove(self, key: int) -> None:
        self.key_map.pop(key, -1)


    def getInorderKeys(self) -> List[int]:
        return list(self.key_map.keys())

