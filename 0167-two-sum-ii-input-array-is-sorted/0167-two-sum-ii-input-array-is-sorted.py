class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for ind, val in enumerate(numbers):
            if target - val in dic:
                return [dic[target-val] + 1, ind + 1]
            else:
                dic[val] = ind