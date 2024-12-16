class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = 100001
        l = 0
        win = 0
        for r in range(len(nums)):
            win += nums[r]
            while win >= target:
                minSize = min(minSize, r-l+1)
                win -= nums[l]
                l += 1
        return 0 if minSize == 100001 else minSize

        