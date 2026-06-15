# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sums = self.path_sum(root)
        return targetSum in sums
        
    def path_sum(self, root):
        if not root:
            return []

        if root.left:
            left = self.path_sum(root.left)
        else:
            left = []
        if root.right:
            right = self.path_sum(root.right)
        else:
            right = []
        
        if not left and not right:
            return [root.val]

        sums = []
        for val in set(left + right):
            curr_num = root.val + val
            sums.append(curr_num)

        return sums

        
