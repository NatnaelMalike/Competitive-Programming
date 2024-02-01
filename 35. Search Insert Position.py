class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        temp=0
        for x in nums:
            if x==target:
                return nums.index(x)
            elif target>x:
                temp=x
            elif target not in nums:
                if target<nums[0]:
                    return 0
                elif target>nums[len(nums)-1]:
                    return len(nums)

        return nums.index(temp)+1
        