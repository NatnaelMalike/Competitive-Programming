class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        maga = Counter(magazine)
        rans = Counter(ransomNote)
        for key in rans:
            if key not in maga:
                return False
            elif maga[key] < rans[key]:
                return False
        return True

        