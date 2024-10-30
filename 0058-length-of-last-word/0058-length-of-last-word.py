class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_s = s.strip()
        arr = new_s.split()
        return len(arr[-1])