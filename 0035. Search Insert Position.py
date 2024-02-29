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
# More Optimized One
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         low = 0
#         high = len(nums) - 1
#         while low <= high:
#             mid = int((low + high) / 2)
#             if nums[mid] == target:
#                 return mid
#             elif target > nums[mid]:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return high + 1
        