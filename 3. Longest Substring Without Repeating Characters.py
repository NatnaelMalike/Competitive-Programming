class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = []
        start = 0
        end = 0
        maxLen = 0
        while(start < len(s) and end < len(s)):
            if s[end] not in temp:
                temp.append(s[end])
                end += 1
                maxLen = max(maxLen, end - start)
            else:
                temp.remove(s[start])
                start += 1
        return maxLen
            
