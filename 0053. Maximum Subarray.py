import sys 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxOfAll = -sys.maxsize - 1
        currentMax = 0
        for i in range(len(nums)):
            currentMax += nums[i]
            maxOfAll = max(maxOfAll, currentMax)
            if currentMax < 0:
                currentMax = 0
        return maxOfAll
