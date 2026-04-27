class LinkedList:
    
    def __init__(self):
        self.data = []

    
    def get(self, index: int) -> int:
        if index >= len(self.data):
            return -1
        return self.data[index]
        

    def insertHead(self, val: int) -> None:
        self.data = [val] + self.data
        

    def insertTail(self, val: int) -> None:
        self.data = self.data + [val]
        

    def remove(self, index: int) -> bool:
        if index >= len(self.data):
            return False
        self.data = self.data[:index] + self.data[(index+1):]
        return True
        

    def getValues(self) -> List[int]:
        return self.data
        
