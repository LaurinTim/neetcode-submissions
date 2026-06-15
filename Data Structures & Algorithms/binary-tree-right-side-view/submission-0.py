# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        res = []
        if root:
            queue.append(root)
        level = 0
        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
                if level == len(res):
                    res.append(curr.val)
            level += 1
        
        return res

        