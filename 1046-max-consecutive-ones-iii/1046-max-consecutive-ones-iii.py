class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        one_freq = 0
        l = 0
        max_len = 0
        for r in range(n):
            if nums[r] == 1:
                one_freq += 1
            if (r - l + 1) - one_freq > k:
                if nums[l] == 1:
                    one_freq -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len
        