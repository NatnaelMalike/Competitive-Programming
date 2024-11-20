class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_win_sum = 0
        for i in range(k):
            curr_win_sum += nums[i]
        maxSum = curr_win_sum
        for i in range(k,len(nums)):
            curr_win_sum += nums[i]
            curr_win_sum -= nums[i-k]
            if maxSum < curr_win_sum:
                maxSum = curr_win_sum
        return maxSum / k

            


        