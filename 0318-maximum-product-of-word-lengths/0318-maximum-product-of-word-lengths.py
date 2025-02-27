class Solution:
    def maxProduct(self, words: List[str]) -> int:
        prod = 0
        for s1 in words:
            for s2 in words:
                if s1 == s2:
                    continue
                if not (set(s1) & set(s2)):
                    prod = max(prod, len(s1) * len(s2))
        return prod

        