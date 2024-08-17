class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        beauty = 0
        numStr = str(num)
        for i in range(len(numStr)-k+1):
            divider = int(numStr[i:i+k])
            if divider != 0 and (num % divider == 0):
                beauty +=1
        return beauty

        