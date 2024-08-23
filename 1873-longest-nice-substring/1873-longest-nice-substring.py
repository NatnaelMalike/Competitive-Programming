class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        longest_str = ''
        for i in range(n):
            for j in range(i+1, n+1):
                sub_str = s[i:j]
                if self.isNiceSubStr(sub_str) and len(sub_str) > len(longest_str):
                    longest_str = sub_str
        return longest_str
    
    def isNiceSubStr(self, sub_str) -> bool:
        sub = set(sub_str)
        for i in sub:
            if i.lower() not in sub or i.upper() not in sub:
                return False
        return True
