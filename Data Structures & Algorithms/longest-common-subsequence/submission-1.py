class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        cache = [[-1 for _ in range(cols)] for _ in range(rows)]

        def memoization(r, c):
            if r >= rows or c >= cols:
                return 0
            if cache[r][c] != -1:
                return cache[r][c]

            if text1[r] == text2[c]:
                seq_len = memoization(r + 1, c + 1) + 1
            else:
                seq_len = max(memoization(r, c + 1), memoization(r + 1, c))
            
            cache[r][c] = seq_len
            return seq_len
        
        return memoization(0, 0)
        