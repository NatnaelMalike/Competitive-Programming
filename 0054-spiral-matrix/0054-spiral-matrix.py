class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        row, col = 0, 0
        UP_END, RIGHT_END, DOWN_END, LEFT_END = 0, n, m, -1
        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
        dire = RIGHT

        while len(ans) < m*n:
            if dire == RIGHT:
                while col < RIGHT_END:
                    ans.append(matrix[row][col])
                    col += 1
                row += 1
                col -= 1
                RIGHT_END -= 1
                dire = DOWN
            elif dire == DOWN:
                while row < DOWN_END:
                    ans.append(matrix[row][col])
                    row += 1
                row -= 1
                col -= 1
                DOWN_END -= 1
                dire = LEFT
            elif dire == LEFT:
                while col > LEFT_END:
                    ans.append(matrix[row][col])
                    col -= 1
                row -= 1
                col += 1
                LEFT_END += 1
                dire = UP
            else:
                while row > UP_END:
                    ans.append(matrix[row][col])
                    row -= 1
                row += 1
                col += 1
                UP_END += 1
                dire = RIGHT
        return ans



        