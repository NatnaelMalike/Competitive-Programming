class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numDict = Counter(nums)
        for num, freq in numDict.items():
            if freq == 1:
                return num
            