class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]
        maxSum = curr_sum
        for i in range(k,len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[i-k]
            if maxSum < curr_sum:
                maxSum = curr_sum
        return maxSum / k

            


        