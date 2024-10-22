class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        numOfPairs = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        numOfPairs += 1
        return numOfPairs

        