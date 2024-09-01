class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPr = 0
        minPrice = float('inf')
        for p in prices:
            if minPrice > p: minPrice = p
            pr = p - minPrice
            if pr > maxPr: maxPr = pr 
        return maxPr


        