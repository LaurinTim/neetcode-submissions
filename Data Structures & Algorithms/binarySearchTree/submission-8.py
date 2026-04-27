class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        prev_node = None
        curr_node = self.root
        if not curr_node:
            self.root = new_node
            return

        while curr_node:
            if curr_node.key == key:
                curr_node.val = val
                return
            if curr_node.key > key:
                if curr_node.left is None:
                    curr_node.left = new_node
                    return
                curr_node = curr_node.left
            else:
                if curr_node.right is None:
                    curr_node.right = new_node
                    return
                curr_node = curr_node.right


    def get(self, key: int) -> int:
        curr_node = self.root
        if not curr_node:
            return -1
        
        while curr_node:
            if key == curr_node.key:
                return curr_node.val
            elif key > curr_node.key:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left

        return -1


    def getMin(self) -> int:
        curr_node = self.root
        if not curr_node:
            return -1
        
        while curr_node.left:
            curr_node = curr_node.left

        return curr_node.val


    def getMax(self) -> int:
        curr_node = self.root
        if not curr_node:
            return -1
        
        while curr_node.right:
            curr_node = curr_node.right

        return curr_node.val


    def remove(self, key: int) -> None:
        def delete(node, key):
            if not node:
                return None
            
            if key < node.key:
                node.left = delete(node.left, key)
            elif key > node.key:
                node.right = delete(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    curr_node = node.right
                    while curr_node.left:
                        curr_node = curr_node.left
                    node.key, node.val = curr_node.key, curr_node.val
                    node.right = delete(node.right, node.key)
                
            return node
                
        self.root = delete(self.root, key)


    def getInorderKeys(self) -> List[int]:
        res = []
        def listCreateDfs(node):
            if node is None:
                return
            listCreateDfs(node.left)
            res.append(node.key)
            listCreateDfs(node.right)
        
        listCreateDfs(self.root)
        return res
