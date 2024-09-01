class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        matrix = []
        i = 0
        for _ in range(m):
            matrix.append(original[i:i+n])
            i += n
        return matrix