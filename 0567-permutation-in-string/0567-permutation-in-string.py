class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        d_s1 = Counter(s1)
        win = Counter(s2[:len(s1)])
        l = 0
        for r in range(len(s1),len(s2)):
            if win == d_s1:
                return True
            if s2[r] in win:
                win[s2[r]] += 1
            else:
                win[s2[r]] = 1
            win[s2[l]] -= 1
            if win[s2[l]] == 0:
                del win[s2[l]]
            l += 1
        if win == d_s1:
                return True
        return False    
        
        