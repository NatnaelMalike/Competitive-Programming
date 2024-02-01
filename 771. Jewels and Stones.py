class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        numDic = {}
        for stone in stones:
            if stone in jewels:
                if stone not in numDic:
                    numDic[stone] = 1
                else:
                    numDic[stone] += 1

        return sum(numDic.values())

        
                
        