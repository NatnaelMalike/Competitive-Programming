class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])

        zRow=set()
        zCol=set()
        for r in range(row):
            for c in range(col):
                if matrix[r][c]==0:
                    zRow.add(r)
                    zCol.add(c)

        for r in range(row):
            for c in range(col):
                if r in zRow or c in zCol:
                    matrix[r][c]=0
    


        