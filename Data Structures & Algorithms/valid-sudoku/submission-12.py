class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rindex = 0
        for c in range(len(board)):
            col = set()
            for r in range(len(board)):
                if board[r][c] in col:
                    return False
                if board[r][c] != ".":
                    col.add(board[r][c])
        for r in range(len(board)):
            row = set()
            for c in range(len(board)):
                if board[r][c] in row:
                    return False
                if board[r][c] != ".":
                    row.add(board[r][c])
        while rindex < len(board):
            cindex = 0
            while cindex < len(board):
                box = set()
                for r in range(rindex, rindex+ 3):
                    for c in range(cindex, cindex+ 3):
                        if board[r][c] in box:
                            return False
                        if board[r][c] != ".":
                            box.add(board[r][c])
                cindex += 3
            rindex += 3
        return True
            


        