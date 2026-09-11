class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        mp = 0
        while l < len(prices) - 1:
            while r < len(prices):
                p = prices[r] - prices[l]
                if p > mp:
                    mp = p
                elif p < 0:
                    l = r
                    break
                r += 1
            
            if r == len(prices):
                l += 1
            
        return mp
        