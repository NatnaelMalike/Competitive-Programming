class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rSum = nums[:]
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        for i in range(-2, -1*(len(nums)+1), -1):
            rSum[i] += rSum[i+1]
        for i in range(len(nums)):
            if nums[i] == rSum[i]:
                return i
        return -1
        
        