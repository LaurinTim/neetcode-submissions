# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = self.buildSubTree(preorder, inorder)
        return root

    def buildSubTree(self, preorder, inorder):
        val = self.getNextRoot(preorder, inorder)
        curr_node = TreeNode(val=val)
        inorder_pos = self.getPos(inorder, val)
        inorder_left = inorder[:inorder_pos]
        inorder_right = inorder[(inorder_pos + 1):]

        if inorder_left:
            curr_node.left = self.buildSubTree(preorder, inorder_left)
        
        if inorder_right:
            curr_node.right = self.buildSubTree(preorder, inorder_right)
        
        return curr_node
        
    def getPos(self, arr, val):
        if val not in arr:
            return None
        i = 0
        while arr[i] != val:
            i += 1
        return i
    
    def getNextRoot(self, preorder, inorder):
        i = 0
        while preorder[i] not in inorder:
            i += 1
        return preorder[i]
