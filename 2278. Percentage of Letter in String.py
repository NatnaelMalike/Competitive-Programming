class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count=0
        for x in s:
            if letter==x:
                count+=1
        per=(count*100)/len(s)
        return int(per)
        
        