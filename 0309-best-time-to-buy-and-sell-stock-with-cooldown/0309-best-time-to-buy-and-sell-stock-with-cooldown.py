class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        cooldown = 0
        sell = 0
        buy = -prices[0]
        
        for i in range(1, len(prices)):
            next_buy = max(buy, cooldown - prices[i])
            next_sell = max(sell, buy + prices[i])
            next_cooldown = max(cooldown, sell)
            
            buy = next_buy
            sell = next_sell
            cooldown = next_cooldown
            
        return max(sell, cooldown) 