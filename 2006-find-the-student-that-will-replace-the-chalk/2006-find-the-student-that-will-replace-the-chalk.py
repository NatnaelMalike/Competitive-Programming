class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        cSum = sum(chalk)
        if len(chalk) == 1:
            return 0
        while k >= cSum:
            k -= cSum
        if k == 0:
            return 0
        for i in range(len(chalk)):
            if chalk[i] <= k:
                k -= chalk[i]
            else:
                return i

        