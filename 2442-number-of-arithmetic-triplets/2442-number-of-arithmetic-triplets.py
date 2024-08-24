class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        unique = 0
        numDict = {}
        for ind,val in enumerate(nums):
            numDict[val] = ind
        for num in nums:
            if (num + diff) in numDict and (num + 2 * diff) in numDict:
                unique += 1
        return unique

        