class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win = []
        l = 0
        r = 0
        max_len = 0
        while r < len(s):
            if s[r] not in win:
                win.append(s[r])
                r += 1
                max_len = max(r-l, max_len)
            else:
                win.remove(s[l])
                l += 1
        return max_len
                
        