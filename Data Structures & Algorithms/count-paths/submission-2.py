class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [0] * n

        for i in range(m):
            curr_row = [0] * n
            curr_row[n - 1] = 1
            for k in range(n - 2, -1, -1):
                curr_row[k] = prev_row[k] + curr_row[k + 1]
            prev_row = curr_row
        
        return curr_row[0]
        