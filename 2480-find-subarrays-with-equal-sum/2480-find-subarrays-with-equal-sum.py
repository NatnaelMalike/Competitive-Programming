class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sumDict = {}
        for i in range(len(nums)-1):
            sum = nums[i] + nums[i+1]
            if sum not in sumDict:
                sumDict[sum] = sum
            else:
                return True
        return False
        