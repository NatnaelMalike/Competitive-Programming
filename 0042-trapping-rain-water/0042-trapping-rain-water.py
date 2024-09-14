class Solution:
    def trap(self, height: List[int]) -> int:
        l_walls = []
        r_walls = []
        max_val = 0
        total = 0
        for h in height:
            if h > max_val:
                max_val = h
            l_walls.append(max_val)
        max_val = 0
        for h in reversed(height):
            if h > max_val:
                max_val = h
            r_walls.append(max_val)
        r_walls.reverse()
        for i in range(len(height)):
            total += max(0,min(l_walls[i], r_walls[i]) - height[i])
        return total



        