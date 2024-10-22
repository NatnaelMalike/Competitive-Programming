class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        answer = []
        l_sum = 0
        for i in range(len(nums)):
            r_sum = total_sum - l_sum - nums[i]
            answer.append(abs(r_sum - l_sum))
            l_sum += nums[i]
    
        return answer 

        