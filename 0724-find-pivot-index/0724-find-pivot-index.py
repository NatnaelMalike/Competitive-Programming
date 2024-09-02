class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        preSum = [0]*n
        preSum[0] = nums[0]
        for i in range(1,n):
            preSum[i] = preSum[i-1] + nums[i]
        for i in range(n):
            if i == 0:
                lSum = 0
            else:
                lSum = preSum[i-1]
            rSum = preSum[n-1] - preSum[i]
            if lSum == rSum:
                return i
        return -1



        
       
        