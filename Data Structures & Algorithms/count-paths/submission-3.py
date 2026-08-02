class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0 for _ in range(n)] for _ in range(m)]

        def memoization(a, b):
            if a == m - 1 and b == n - 1:
                return 1
            if a >= m or b >= n:
                return 0
            if cache[a][b] != 0:
                return cache[a][b]
            
            res = memoization(a + 1, b) + memoization(a, b + 1)
            cache[a][b] = res
            return res
                
        return memoization(0, 0)
