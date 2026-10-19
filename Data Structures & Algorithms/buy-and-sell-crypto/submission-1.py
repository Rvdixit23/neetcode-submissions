class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        top = 0
        L = 0
        R = 1
        while R < len(prices):
            top = max(top, prices[R] - prices[L])
            if prices[R] < prices[L]:
                L = R
                R = L + 1
            else:
                R += 1
        return top