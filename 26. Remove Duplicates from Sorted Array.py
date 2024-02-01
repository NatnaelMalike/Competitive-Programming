class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for x in range(1,len(nums)):
            if nums[x]!= nums[i]:
                i+=1
                nums[i]=nums[x]
        return i+1
                
        