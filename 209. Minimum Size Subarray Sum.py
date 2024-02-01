class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        beg = 0
        sum = 0
        minL = 100001
        for i in range(len(nums)):
            sum += nums[i]
            while(sum >= target):
                minL = min(minL, i - beg + 1)
                sum -= nums[beg]
                beg += 1
        return minL if minL != 100001 else 0
