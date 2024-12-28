class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            covered = False
            for sta, end in ranges:
                if sta <= i <= end:
                    covered = True
                    break
            if not covered:
                return False
        return True
        