from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))

        if grid[0][0] == 1:
            return -1

        length = 1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length
                
                neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1], 
                    [1, 1], [1, -1], [-1, 1], [-1, -1]]
                for rd, cd in neighbours:
                    rc, cc = r + rd, c + cd
                    
                    if (min(rc, cc) < 0
                        or rc == rows or cc == cols
                        or (rc, cc) in visit
                        or grid[rc][cc] == 1):
                        continue
                    
                    queue.append((rc, cc))
                    visit.add((rc, cc))
            
            length += 1
            
        return -1