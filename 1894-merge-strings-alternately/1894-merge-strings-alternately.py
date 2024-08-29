class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        n = min(n1,n2)
        s = ''
        for i in range(n):
            s += word1[i] + word2[i]
        if n1 == n2:
            return s
        elif n1 > n2:
            s += word1[n2:]
        else:
            s += word2[n1:]
        return s
