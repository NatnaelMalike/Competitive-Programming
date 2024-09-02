class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        tSum = sum(nums)
        lSum = 0
        for i in range(len(nums)):
            rSum = tSum - lSum - nums[i]
            if rSum == lSum:
                return i
            lSum += nums[i]
        return -1


        