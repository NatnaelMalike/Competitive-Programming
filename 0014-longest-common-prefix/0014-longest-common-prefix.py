class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        co_pre = ""
        s = sorted(strs)
        first = s[0]
        last = s[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return co_pre
            co_pre += first[i]
        return co_pre
        