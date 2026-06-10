# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        _, val = self.getkthSmallest(root, k)
        return val
        
    def getkthSmallest(self, root, k, c=0, val=None):
        if not root:
            return c, None
        c, val = self.getkthSmallest(root.left, k, c, val)
        c += 1
        if c == k:
            return c, root.val
        elif val:
            return c, val
        c, val = self.getkthSmallest(root.right, k, c, val)
        return c, val
        


        
        