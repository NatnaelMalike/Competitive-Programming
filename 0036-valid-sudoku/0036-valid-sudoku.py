class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            uniq = []
            for j in range(9):
                if board[i][j] in uniq:
                    return False
                elif board[i][j] != '.':
                    uniq.append(board[i][j])
        for i in range(9):
            uniq = []
            for j in range(9):
                if board[j][i] in uniq:
                    return False
                elif board[j][i] != '.':
                    uniq.append(board[j][i])
        starter = [
            [0,0], [0,3], [0,6],
            [3,0], [3,3], [3,6],
            [6,0], [6,3], [6,6]
        ]
        for i,j in starter:
            uniq = []
            for r in range(i, i+3):
                for c in range(j, j+3):
                    if board[r][c] in uniq:
                        return False
                    elif board[r][c] != '.':
                        uniq.append(board[r][c])
        return True

                
        
        