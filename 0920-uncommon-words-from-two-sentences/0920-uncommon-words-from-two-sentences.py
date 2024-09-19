class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        h1 = s1.split(" ") + s2.split(" ")
        h2 = Counter(h1)
        res = []
        for key,val in h2.items():
            if val == 1:
                res.append(key)
        return res

        