class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, count):
            if (min(r, c) < 0
                or r >= rows
                or c >= cols
                or grid[r][c] == 0):
                return count
            grid[r][c] = 0
            count += 1
            count = dfs(r + 1, c, count)
            count = dfs(r - 1, c, count)
            count = dfs(r, c + 1, count)
            count = dfs(r, c - 1, count)
            return count
        
        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                curr_area = dfs(row, col, 0)
                if curr_area > max_area:
                    max_area = curr_area
        return max_area