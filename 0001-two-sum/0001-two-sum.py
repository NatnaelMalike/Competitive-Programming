class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, element in enumerate(nums):
            if(target - element in dic):
                return [index, dic[target-element]]
            else:
                dic[element] = index
        