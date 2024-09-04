class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obs_set = set(map(tuple, obstacles))
        x, y, d, max_dist = 0, 0, 0, 0

        for c in commands:
            if c == -2:
                d = (d - 1) % 4
            elif c == -1:
                d = (d + 1) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(c):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) not in obs_set:
                        x, y = nx, ny
                        max_dist = max(max_dist, x * x + y * y)
                    else:
                        break

        return max_dist
