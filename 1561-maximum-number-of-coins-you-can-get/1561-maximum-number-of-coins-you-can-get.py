class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        tot = 0
        for i in range(len(piles)//3):
            tot += piles[-(2*i+2)]
        return tot

       
        