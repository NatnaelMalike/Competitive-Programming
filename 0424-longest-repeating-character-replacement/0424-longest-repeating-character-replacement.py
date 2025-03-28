class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_count = 0
        char_dict = defaultdict(int)
        for r,val in enumerate(s):
            char_dict[val] += 1
            if char_dict[val] > max_count:
                max_count = char_dict[val]

            if (r-l+1) - max_count > k:
                char_dict[s[l]] -= 1
                l += 1

        return len(s) - l
        