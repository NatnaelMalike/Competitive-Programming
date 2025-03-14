class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = -1
        for n in nums:
            sq_str = 1
            while n*n in nums:
                sq_str += 1
                n = n*n
            ans = max(sq_str, ans)
        return ans if ans > 1 else -1
        