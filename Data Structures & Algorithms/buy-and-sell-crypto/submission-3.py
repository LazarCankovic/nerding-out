class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        l, r = 0, 1
        
        # go through all the prices
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxp = max(maxp, profit)
            else:
                l = r
            r += 1
        return maxp
            
            