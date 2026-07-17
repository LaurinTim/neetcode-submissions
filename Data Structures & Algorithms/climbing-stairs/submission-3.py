class Solution:
    def climbStairs(self, n: int) -> int:
        cache = dict()

        def memoization(k, cache):
            if k <= 1:
                return 1
            if k in cache:
                return cache[k]
            
            cache[k] = memoization(k - 1, cache) + memoization(k - 2, cache)
            return cache[k]
        
        return memoization(n, cache)
        