class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        for i,v in enumerate(nums):
            if v == target:
                res.append(i)
        return res
