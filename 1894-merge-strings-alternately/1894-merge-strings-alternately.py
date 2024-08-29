class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        isWord1 = True
        a, b = 0, 0
        s = []
        while a < n1 and b < n2:
            if isWord1:
                s.append(word1[a])
                a += 1
                isWord1 = False
            else:
                s.append(word2[b])
                b += 1
                isWord1 = True
        while a < n1:
            s.append(word1[a])
            a += 1
        while b < n2:
            s.append(word2[b])
            b += 1
        return "".join(s)
