class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        maxN = max(nums)
        histoG = [0] * (maxN + 1)
        
        for i in nums:
            histoG[i] += 1

        j = 0
        for i in range(maxN + 1):
            for _ in range(histoG[i]):
                nums[j] = i
                j += 1
       