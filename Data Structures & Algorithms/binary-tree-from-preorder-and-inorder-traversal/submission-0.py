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
        val = preorder[0]
        curr_node = TreeNode(val=val)
        inorder_pos = self.getPos(inorder, val)
        inorder_left = inorder[:inorder_pos]
        inorder_right = inorder[(inorder_pos + 1):]

        if inorder_left:
            preorder_left = self.getSubPreorder(inorder_left, preorder)
            curr_node.left = self.buildSubTree(preorder_left, inorder_left)
        
        if inorder_right:
            preorder_right = self.getSubPreorder(inorder_right, preorder)
            curr_node.right = self.buildSubTree(preorder_right, inorder_right)
        
        return curr_node
        
    def getPos(self, arr, val):
        if val not in arr:
            return None
        i = 0
        while arr[i] != val:
            i += 1
        return i
    
    def getSubPreorder(self, sub_inorder, preorder):
        sub_preorder = []
        for val in preorder[1:]:
            if val in sub_inorder:
                sub_preorder.append(val)
        
        return sub_preorder
