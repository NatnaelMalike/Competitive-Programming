class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        dict = {}
        for x in nums:
            if x in dict:
                dict[x] += 1
                count += dict[x]
            else:
                dict[x] = 0
        return count