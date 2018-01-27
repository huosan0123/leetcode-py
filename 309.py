class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        copied.
        """
        cash0_pre, cash0, hold1 = 0, 0, float("-inf")  # initialization is key!
        for price in prices:
            old = cash0
            cash0 = max(cash0, hold1 + price)
            hold1 = max(hold1, cash0_pre - price)
            cash0_pre = old
        return cash0
