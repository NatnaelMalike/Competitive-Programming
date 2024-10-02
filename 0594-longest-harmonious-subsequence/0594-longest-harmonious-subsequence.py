class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = Counter(nums)
        res = 0
        for i in dic:
            if i + 1 in dic:
                res = max(res, dic[i] + dic[i+1])
        return res




