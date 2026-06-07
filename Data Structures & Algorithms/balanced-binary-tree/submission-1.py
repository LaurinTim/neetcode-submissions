# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return bool(self.getBalance(root))
    
    def getBalance(self, root):
        if not root:
            return 1
        
        left = self.getBalance(root.left)
        right = self.getBalance(root.right)
        if left and right and abs(left - right) <= 1:
            return max(left, right) + 1
        return False