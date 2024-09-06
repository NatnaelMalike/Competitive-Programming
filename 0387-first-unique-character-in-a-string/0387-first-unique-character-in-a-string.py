class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = Counter(s)
        for index, value in enumerate(s):
            if dic[value] == 1:
                return index
        return -1
        