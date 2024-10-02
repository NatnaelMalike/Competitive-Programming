class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = Counter(nums)
        n1 = sorted(n.keys())
        if len(n1) <= 1:
            return 0
        res = 0
        for i in range(len(n1)-1):
            if n1[i+1] - n1[i] == 1:
                res = max(res, n[n1[i+1]] + n[n1[i]])
        return res



