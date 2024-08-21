class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        res = []
        pDict = {}
        for i in p:
            if i not in pDict:
                pDict[i] = 1
            else:
                pDict[i] += 1

        for i in range(len(s)-k+1):
            isAna = True
            curWin = s[i:k+i]
            for j in set(curWin):
                if j not in pDict:
                    isAna = False
                elif curWin.count(j) != pDict[j]:
                    isAna = False
            if isAna:
                res.append(i)
        return res

        