class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        newArr = sorted(nums)
        answer = []
        for i in nums:
            answer.append(newArr.index(i))
        return answer


# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         newNums = sorted(nums)
#         return [newNums.index(ele) for ele in nums]