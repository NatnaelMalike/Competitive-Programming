class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        pairs = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            end = i + 1
            while(end < len(nums) and abs(nums[end] - nums[i]) < k): end += 1
            if end == len(nums): break
            if abs(nums[end] - nums[i]) == k: pairs += 1
        return pairs