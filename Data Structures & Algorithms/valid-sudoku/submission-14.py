class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):

                value = board[r][c]

                # Ignore empty cells
                if value == ".":
                    continue

                # Determine which 3x3 box contains this cell
                box_row = r // 3
                box_col = c // 3

                # Check whether the value is duplicated
                if (value in rows[r] or
                    value in cols[c] or
                    value in boxes[box_row][box_col]):
                    return False

                # Add the value to all three tracking sets
                rows[r].add(value)
                cols[c].add(value)
                boxes[box_row][box_col].add(value)

        return True