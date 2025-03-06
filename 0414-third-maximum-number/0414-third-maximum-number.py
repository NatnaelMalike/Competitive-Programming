class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = list(set(nums))
        if len(a) < 3:
            return max(a)
        a.sort()
        return a[-3]

        