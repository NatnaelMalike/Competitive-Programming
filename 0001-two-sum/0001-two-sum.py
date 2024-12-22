class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in nums:
            for y in range(1,len(nums)):
                if x+nums[y]==target:
                    if nums.index(x)==y:
                        continue
                    return [nums.index(x),y]

                
