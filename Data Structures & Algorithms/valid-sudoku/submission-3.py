class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_rows = {i: set() for i in range(9)}
        seen_cols = {i: set() for i in range(9)}
        seen_boxs = {(i, j): set() for i in range(3) for j in range(3)}

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                if value in seen_rows[r] or value in seen_cols[c] or value in seen_boxs[(r//3, c//3)]:
                    return False
                seen_rows[r].add(value)
                seen_cols[c].add(value)
                seen_boxs[(r//3, c//3)].add(value)
        
        return True