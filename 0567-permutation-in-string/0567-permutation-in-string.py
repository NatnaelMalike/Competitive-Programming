class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        win = Counter(s2[:len(s1)])
        for i in range(len(s2)-len(s1)):
            if s1_count == win:
                return True
            
            win[s2[i]] -= 1
            if win[s2[i]] == 0:
                del win[s2[i]]
            win[s2[i+len(s1)]] += 1
        return win == s1_count



