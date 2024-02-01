class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if(len(nums) < 3):
            return []
        solution = []
        for i in range(len(nums)):
            if(nums[i] > 0):
                break
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            first = i + 1
            last = len(nums) - 1
            while(first < last):
                if(nums[i] + nums[first] + nums[last] > 0):
                    last -= 1
                elif(nums[i] + nums[first] + nums[last] < 0):
                    first += 1
                else:
                    solution.append([nums[i], nums[first], nums[last]])
                    firstEle = nums[first]
                    lastEle = nums[last]
                    while first < last and firstEle == nums[first] :
                        first += 1
                    while first < last and lastEle == nums[last]:
                        last -= 1
            
        return solution