class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[0 for _ in range(cols)] for _ in range(rows)]

        def memoization(r, c):
            if r >= rows or c >= cols:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1
            if cache[r][c] != 0:
                return cache[r][c]
            
            paths = memoization(r + 1, c) + memoization(r, c + 1)
            cache[r][c] = paths
            return paths
        
        return memoization(0, 0)
        