class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numDict = Counter(nums)
        for i in numDict:
            if numDict[i] == 1:
                return i
            