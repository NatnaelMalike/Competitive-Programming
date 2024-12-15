class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        pCount = Counter(p)
        currWin = Counter()
        anas = []
    
        for i in range(len(s)):
            currWin[s[i]] += 1

            if i >= k:
                if currWin[s[i-k]] == 1:
                    del currWin[s[i-k]]
                else:
                    currWin[s[i-k]] -= 1

            if currWin == pCount:
                anas.append(i-k+1)

        return anas
        
        