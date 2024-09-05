class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        mSum = sum(rolls)
        res = []
        nSum = mean * (n + len(rolls)) - mSum
        if nSum > 6*n or nSum < n:
            return []
        res = [nSum // n]*n
        rem = nSum % n
        for i in range(rem):
            res[i] += 1
        return res


        