class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        r = 0
        n = len(chars)
        while r < n:
            char = chars[r]
            cnt = 0

            while r < n and chars[r] == char:
                cnt += 1
                r += 1
            chars[l] = char
            l += 1

            if cnt > 1:
                for x in str(cnt):
                        chars[l] = x
                        l += 1
        return l
        
            


