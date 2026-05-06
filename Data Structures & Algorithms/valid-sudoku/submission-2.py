import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                board_val = board[r][c]
                if board_val == ".":
                    continue
                if board_val in rows[r] or board_val in cols[c] or board_val in squares[(r//3, c//3)]:
                    return False
                rows[r].add(board_val)
                cols[c].add(board_val)
                squares[(r//3, c//3)].add(board_val)
        return True

                 