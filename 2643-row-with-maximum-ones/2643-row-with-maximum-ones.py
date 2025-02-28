class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        out = [0,0]
        for idx, row in enumerate(mat):
            if row.count(1) > out[1]:
                out[0] = idx
                out[1] = row.count(1)
        return out


            