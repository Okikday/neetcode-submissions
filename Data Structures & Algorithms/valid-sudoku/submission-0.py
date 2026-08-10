class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        size = len(board)

        for i in range(size):

            # check a square
            square = set()
            r, c = (i // 3) * 3, (i % 3) * 3

            for _ in range(3):
                for x in range(3):
                    if board[r][c+x] in square:
                        return False
                    if board[r][c+x] == ".":
                        pass
                    else:
                        square.add(board[r][c+x])
                r += 1


            col, row = set(), set()

            for x in range(size):
                if board[i][x] in row or board[x][i] in col:
                    return False

                if board[i][x] == ".":
                    pass
                else:
                    row.add(board[i][x])

                if board[x][i] == ".":
                    pass
                else:
                    col.add(board[x][i])
               
            i += 1

        return True