class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        end = len(numbers) - 1
        beg = 0
        while(end > beg):
            if numbers[beg] + numbers[end] > target:
                end -= 1
            elif numbers[beg] + numbers[end] == target:
                return[beg + 1, end + 1]
            else: beg += 1
        
