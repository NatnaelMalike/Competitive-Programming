class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, element in enumerate(nums):
            if(target - element in dict):
                return [index, dict[target-element]]
            else:
                dict[element] = index
        
