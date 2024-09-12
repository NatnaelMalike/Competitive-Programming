class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic = Counter(nums)
        ind = 0
        for i in range(3):
            for _ in range(dic[i]):
                nums[ind] = i
                ind += 1


        