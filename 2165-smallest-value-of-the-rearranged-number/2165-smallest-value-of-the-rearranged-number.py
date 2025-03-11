class Solution:
    def smallestNumber(self, num: int) -> int:
        s = sorted(str(abs(num)))
        if num <= 0:
            return -int(''.join(s[::-1]))
        for i in range(len(s)):
            if s[i] != '0':
                s[0], s[i] = s[i], s[0]
                break
        return int(''.join(s))
        

        