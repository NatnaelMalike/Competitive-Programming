class Solution:
    def longestPalindrome(self, s: str) -> int:
        letDict ={}
        length = 0
        odd = False
        for i in s:
            if i in letDict:
                letDict[i] += 1
            else:
                letDict[i] = 1
        for key, value in letDict.items():
            if value % 2 == 0:
                length += value
            else:
                length += value - 1
                odd = True
        if odd:
            length += 1
        return length

        