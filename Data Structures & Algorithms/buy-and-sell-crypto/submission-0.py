class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        # While right isn't the end
        while right < len(prices):
            # Flipped right/left at first, right should be current max left current min, so max - min
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)

            if profit < 0:
                # Shift to where right is because it's lowest price
                left = right
            
            # Shift right
            right += 1
        return max_profit

