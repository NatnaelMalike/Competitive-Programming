class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        eSum = 0
        tSum = sum(nums)
        for i in range(n+1):
            eSum += i
        return eSum - tSum


        