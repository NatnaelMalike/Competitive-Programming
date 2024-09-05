class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        mSum = 0
        res = []
        for i in rolls:
            mSum += i
        nSum = mean * (n + len(rolls)) - mSum
        if nSum > 6*n or nSum < n:
            return []
        else:
            val = nSum // n
            rem = nSum % n
            res = [val]*n
            for i in range(rem):
                res[i] += 1
        return res


        