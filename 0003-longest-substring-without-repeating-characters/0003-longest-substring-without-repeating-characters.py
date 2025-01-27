class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win = set()
        l = 0
        max_len = 0
        for r in range(len(s)):
            while s[r] in win:
                win.remove(s[l])
                l += 1
            win.add(s[r])
            max_len = max(max_len, len(win))
            
      
        return max_len
                
        