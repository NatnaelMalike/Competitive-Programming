class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            elif maxProfit < prices[r] - prices[l]: 
                maxProfit = prices[r] - prices[l]
            r += 1
        return maxProfit


        