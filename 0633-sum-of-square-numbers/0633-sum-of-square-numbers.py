class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        r = math.ceil(math.sqrt(c))
        l = 0
        while l <= r:
            if l**2 + r**2 == c:
                return True
            elif l**2 + r**2 > c:
                r -= 1
            else:
                l += 1
        return False

        
        