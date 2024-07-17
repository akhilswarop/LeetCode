class Solution:
    def maxProfit(self, prices):
        maxProfit = 0
        profits = []
        l,r = 0,1
        while r < len(prices) - 1:
            if prices[l] > prices[r]:
                l = r
            r+=1
            profit = prices[r] - prices[l]
            maxProfit = max(profit, maxProfit)
        return maxProfit


            

            

            


s = Solution()
print(s.maxProfit([5,1,5,6,7,1,10]))