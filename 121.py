class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff, cheapest = 0, 99999999
        for p in prices:
            if cheapest < p:
                diff = max(diff, p - cheapest)
            else:
                cheapest = p
        return diff
