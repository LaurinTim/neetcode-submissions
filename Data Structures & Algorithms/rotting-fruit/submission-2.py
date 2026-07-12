from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = set()
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        minutes = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for rd, cd in neighbours:
                    rc, cc = r + rd, c + cd
                    if (min(rc, cc) < 0
                        or rc == rows or cc == cols
                        or grid[rc][cc] != 1):
                        continue
                    
                    grid[rc][cc] = 2
                    queue.append((rc, cc))
                    fresh.remove((rc, cc))
            
            minutes += 1

        if not fresh:
            return max(0, minutes - 1)
        return -1

        