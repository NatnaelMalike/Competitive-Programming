class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])
        imgM = [[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                total = 0
                count = 0
                for x in [i-1, i, i+1]:
                    for y in [j-1, j, j+1]:
                        if 0 <= x < row and 0 <= y < col:
                            total += img[x][y]
                            count += 1
                avg = total // count
                imgM[i][j] = avg
        return imgM
        