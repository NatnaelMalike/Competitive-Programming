class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        col = len(mat[0])
        row = len(mat)
        upward = True
        i = 0
        j = 0
        res = []
        cells = 0
        while cells < col*row:
            if upward:
                while i >= 0 and j < col:
                    res.append(mat[i][j])
                    cells += 1
                    i -= 1
                    j += 1
                if j == col:
                    i += 2
                    j -= 1
                if i < 0:
                    i += 1
                upward = False
            else:
                while i < row and j >= 0:
                    res.append(mat[i][j])
                    cells += 1
                    i += 1
                    j -= 1
                if i == row:
                    j += 2
                    i -= 1
                if j < 0:
                    j += 1 
                upward = True
        return res

        