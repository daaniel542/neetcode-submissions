class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # window size can be any large 
        left = 0
        right = 1
        maxP = 0

        while right < len(prices):
            if prices[left] < prices [right]:
                profit = prices [right] - prices[left]
                maxP = max(maxP, profit)
            else:
                left = right
            right +=1  
        return maxP

            