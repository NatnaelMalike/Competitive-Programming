class Solution:
    def isPalindrome(self, s, l, r)-> bool:
        while(l < r):
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1
        while(l < r):
            if s[l] == s[r]:
                l += 1
                r -= 1
            else: 
                if self.isPalindrome(s, l+1, r):
                    return True
                if self.isPalindrome(s, l, r-1):
                    return True
                return False
            
        return True

    