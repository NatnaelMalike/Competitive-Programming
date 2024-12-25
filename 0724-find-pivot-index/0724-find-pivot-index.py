class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pSum = nums[:]
        for i in range(1,n):
            pSum[i] += pSum[i-1] 
        for i in range(n):
            if pSum[i] - nums[i] == pSum[-1] - pSum[i]:
                return i
        return -1