class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        col = len(matrix[0])
        row = len(matrix)
        transposeM = [[0]*row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                transposeM[j][i] = matrix[i][j]
        return transposeM
        