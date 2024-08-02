class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums) -1
            num = -1*nums[i]
            while l < r:
                if num > (nums[l] + nums[r]):
                    l += 1
                elif num < (nums[l] + nums[r]):
                    r -= 1
                else:
                    solution.append([nums[i],nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

        return solution