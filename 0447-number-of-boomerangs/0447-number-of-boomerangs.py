class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        for p1 in points:
            same_d = defaultdict(int)
            for p2 in points:
                if p1 == p2:
                    continue
                d = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                same_d[d] += 1
            for ds in same_d.values():
                total += ds*(ds-1)
        return total
