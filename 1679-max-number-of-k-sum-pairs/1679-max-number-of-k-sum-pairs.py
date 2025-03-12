class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        cnt = 0
        while l < r:
            s = nums[r] + nums[l]
            if s == k:
                cnt += 1
                l += 1
                r -= 1
            elif s > k:
                r -= 1
            else: 
                l += 1
        return cnt
