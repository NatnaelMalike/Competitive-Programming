class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        newArr = sorted(nums)
        beg = -1
        end = 0
        for i in range(len(nums)):
            if nums[i] != newArr[i]:
                beg = i
                break
        if beg == -1:
            return 0
        for i in range(len(nums)-1,0,-1):
            if nums[i] != newArr[i]:
                end = i
                break
        return end - beg + 1  
