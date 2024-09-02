class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        cSum = sum(chalk)
        k %= cSum
        for i in range(len(chalk)):
            if chalk[i] <= k:
                k -= chalk[i]
            else:
                return i

        