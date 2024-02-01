class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = dict()
        
        for i in s:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for i in t:
            if i in seen:
                seen[i] -=1
            else:
                return False
        for i in seen:
            
            if seen[i] != 0:
                return False
        
        return True
        