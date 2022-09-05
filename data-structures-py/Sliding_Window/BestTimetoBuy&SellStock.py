class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        maxP = 0
        
        # while right is not at the end of array
        while r < len(prices):
            # if left is less then right we can calc a profit
            # check if its greater then cur maxP
            if prices[l] < prices[r]:
                # calc profit
                profit = prices[r] - prices[l]
                # check for new max? max vs current and new calculated profit
                maxP = max(maxP, profit)
            # else move left pointer to right
            else:
                l = r
            # increment right pointer
            r += 1
        #return max profit
        return maxP



sol_class = Solution()

prices = [7,1,5,3,6,4]
sol_class.maxProfit(prices)