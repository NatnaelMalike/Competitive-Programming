class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        lPro = [1]*len(nums)
        rPro = [1]*len(nums)
        l = 1
        for i in range(1,len(nums)):
            lPro[i] = lPro[i-1] * nums[i-1]
        r = 1
        for i in range(len(nums)-2,-1,-1):
            rPro[i] = rPro[i+1] * nums[i+1]
        for i in range(len(nums)):
            answer.append(lPro[i]*rPro[i])
        return answer
        
        
        