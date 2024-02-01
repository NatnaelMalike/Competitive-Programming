class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        xArr = nums[slice(n)]
        yArr = nums[slice(n,2*n)]
        shuffledArr = []
        for i in range(len(nums)):
            if(i%2 == 0):
                shuffledArr.append(xArr[ceil(i/2)])
            else:
                shuffledArr.append(yArr[floor(i/2)])
        return shuffledArr


        