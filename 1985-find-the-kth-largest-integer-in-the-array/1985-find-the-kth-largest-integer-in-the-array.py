class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key = lambda x: int(x))
        return str(nums[-1 * k])

        