class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        total = 0
        n = len(word)
        for l in range(n):
            if word[l] not in vowels:
                continue
            unique = set()
            for r in range(l, n):
                if word[r] not in vowels:
                    break
                unique.add(word[r])
                if len(unique) == 5:
                    total += 1
        return total

        