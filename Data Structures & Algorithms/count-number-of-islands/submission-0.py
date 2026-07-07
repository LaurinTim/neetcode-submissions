class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (min(r, c) < 0
                or r >= rows
                or c >= cols
                or (r, c) in visited
                or grid[r][c] == "0"):
                return

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if (row, col) in visited:
                    continue
                
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
        
        return islands
        