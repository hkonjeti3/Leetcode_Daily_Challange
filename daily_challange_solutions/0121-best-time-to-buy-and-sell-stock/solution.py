class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minVal=prices[0]
        for idx in range(1,len(prices)):
            profit=max(profit,prices[idx]-minVal)
            if prices[idx]<minVal:
                minVal=prices[idx]

        return profit
        
