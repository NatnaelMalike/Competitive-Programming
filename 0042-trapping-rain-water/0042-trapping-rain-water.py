class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_walls = [0] * n
        r_walls = [0] * n
        l = 0
        r = 0
        total = 0
        for i in range(n):
            j = -i -1
            l_walls[i] = l 
            r_walls[j] = r 
            l = max(l, height[i])
            r = max(r, height[j])
        for i in range(n):
            total += max(0,min(l_walls[i], r_walls[i]) - height[i])
        return total



        