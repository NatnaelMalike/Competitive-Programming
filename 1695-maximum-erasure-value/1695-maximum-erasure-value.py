class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        unique = set()
        l = 0
        curr = 0
        score = 0
        for r in range(n):
            while nums[r] in unique:
                unique.remove(nums[l])
                curr -= nums[l]
                l += 1
            unique.add(nums[r])
            curr += nums[r]
            score = max(curr, score)
        return score
            


        