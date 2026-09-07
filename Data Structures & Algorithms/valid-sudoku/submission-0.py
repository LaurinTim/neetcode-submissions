class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = board[i]
            col = [val[i] for val in board]
            row_freqs = self._count_frequencies(row)
            col_freqs = self._count_frequencies(col)
            if ((row_freqs and max(row_freqs.values()) > 1)
                or (col_freqs and max(col_freqs.values()) > 1)):
                return False
        
        for i in range(3):
            for k in range(3):
                box = [board[3*i + r][3*k + c] for r in range(3) for c in range(3)]
                box_freqs = self._count_frequencies(box)
                if box_freqs and max(box_freqs.values()) > 1:
                    return False
        
        return True

    
    def _count_frequencies(self, arr):
        freqs = defaultdict(int)
        for val in arr:
            if val != ".":
                freqs[val] += 1
        
        return freqs

        