class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum  = 0
        start = 0
        for i in range(k):
            sum += nums[i]
        temp = sum
        while(start+k < len(nums)):
            temp = temp-nums[start]+nums[start+k]
            sum = max(sum,temp)
            start += 1
        return sum / k
