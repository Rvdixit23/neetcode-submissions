class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Greedy approach
        # Check if the next element is greater than current element
        # Buy if price is higher next day
        index = 0
        profit = 0
        while index < len(prices) - 1:
            if prices[index + 1] > prices[index]:
                profit += prices[index + 1] - prices[index]
            index += 1
        return profit