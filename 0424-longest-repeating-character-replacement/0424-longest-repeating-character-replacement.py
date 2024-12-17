class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_count = 0
        max_len = 0
        char_dict = {}
        for r in range(len(s)):
            char_dict[s[r]] = char_dict.get(s[r], 0) + 1
            max_count = max(max_count, char_dict[s[r]])

            while (r-l+1) - max_count > k:
                char_dict[s[l]] -= 1
                l += 1

            max_len = max(max_len, r-l+1)

        return max_len
        