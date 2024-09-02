class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lSum, rSum = 0, sum(nums)
        for i,v in enumerate(nums):
            rSum -= v
            if lSum == rSum:
                return i
            lSum += v
        return -1
        