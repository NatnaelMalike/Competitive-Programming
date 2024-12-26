class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        pSum = [0] * (n)
        for l, r, k in shifts:
            k = 1 if k == 1 else -1
            pSum[l] += k
            if r+1 < n:
                pSum[r+1] -= k
        for i in range(1, n):
            pSum[i] += pSum[i - 1]
        res = list(s)
        for i in range(n):
            res[i] = chr((ord(res[i]) - ord('a') + pSum[i]) % 26 + ord('a'))
        return "".join(res)
      
        
        