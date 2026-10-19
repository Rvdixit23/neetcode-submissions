class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        top = 0
        for L in range(len(prices)):
            for R in range(L + 1, len(prices)):
                top = max(prices[R] - prices[L], top)
        return top