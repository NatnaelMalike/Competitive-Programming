class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        longStr = ''.join(words)
        myDict = {}
        for i in longStr:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1

        for val in myDict.values():
            if val % len(words) != 0:
                return False
        return True

      