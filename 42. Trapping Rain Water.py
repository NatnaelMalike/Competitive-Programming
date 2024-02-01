class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        right = []
        maximum = 0
        totalSum = 0
        for i in height:
            maximum = max(i,maximum)
            left.append(maximum)
        maximum = 0
        for i in reversed(height):
            maximum = max(i,maximum)
            right.append(maximum)
        right.reverse()
        for i in range(len(height)):
            if(height[i] < min(left[i],right[i])):
                totalSum += min(left[i],right[i]) - height[i] 
        return totalSum

        