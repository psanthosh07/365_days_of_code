class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        s=prices[0]
        p=0
        for i in range(0,l):
            if s < prices[i]:
                p+=prices[i]-s
            s=prices[i]

        return p
        
