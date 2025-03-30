class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        p_sum = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                p_sum[i][j] = matrix[i][j]
                if i > 0:
                    p_sum[i][j] += p_sum[i-1][j]
                if j > 0:
                    p_sum[i][j] += p_sum[i][j-1]
                if i > 0 and j > 0:
                    p_sum[i][j] -= p_sum[i-1][j-1]
        self.p_sum = p_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.p_sum[row2][col2]
        if row1 == 0:
            return self.p_sum[row2][col2] - self.p_sum[row2][col1-1]
        if col1 == 0:
            return self.p_sum[row2][col2] - self.p_sum[row1-1][col2]
        return self.p_sum[row2][col2] - self.p_sum[row1-1][col2] - self.p_sum[row2][col1-1] + self.p_sum[row1-1][col1-1]

        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)