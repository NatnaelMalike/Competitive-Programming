class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        pCount = Counter(p)
        currWin = Counter(s[:k])
        anas = []
        if pCount == currWin:
            anas.append(0)
    
        for i in range(len(s)-k):
            if s[i+k] in currWin:
                currWin[s[i+k]]  = currWin[s[i+k]] + 1
            else:
                currWin[s[i+k]] = 1

            if currWin[s[i]] == 1:
                currWin.pop(s[i])
            else:
                currWin[s[i]] = currWin[s[i]] - 1
                
            if currWin == pCount:
                anas.append(i+1)
        return anas
        
        