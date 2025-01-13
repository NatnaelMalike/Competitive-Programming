class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        l = 0
        while r >= l:
            mid = (l + r)// 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return r + 1
        