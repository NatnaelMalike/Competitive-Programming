class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        ans = 0
        for num in ns:
            if num - 1 not in ns:
                nex = num + 1
                while nex in ns:
                    nex += 1
                ans = max(ans, nex-num)
        return ans


       
        