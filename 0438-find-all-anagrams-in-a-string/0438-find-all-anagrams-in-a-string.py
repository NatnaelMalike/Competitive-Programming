class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c_p = Counter(p)
        win = Counter(s[: len(p)])
        res = []
        l = 0
        for r in range(len(p), len(s)):
            if win == c_p:
                res.append(l)

            win[s[r]] += 1

            win[s[l]] -= 1

            if win[s[l]] == 0:
                del win[s[l]]
            
            l += 1

        if win == c_p:
            res.append(l)
        return res
