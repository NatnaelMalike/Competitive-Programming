class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sl = sorted(nums)
        return sl[len(nums)-k]