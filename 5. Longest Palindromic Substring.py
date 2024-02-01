class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrom = ""
        j = 0
        str = ""
        for j in range(0,len(s)):
            str = ""
            for i in range(j,len(s)):
                str += s[i]
                if(str == str[::-1]):
                    if(len(palindrom) < len(str)):
                        palindrom = str
            
        return palindrom
