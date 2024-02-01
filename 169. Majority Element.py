class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxi = 0
        num = 0
        newSet = set(nums)
        for i in newSet:
            if(nums.count(i) >  len(nums)/2):
                if(maxi < nums.count(i)):
                    maxi = nums.count(i)
                    num = i
        return num