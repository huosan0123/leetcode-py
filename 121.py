class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
<<<<<<< HEAD
        """
        diff, cheapest = 0, 99999999
        for p in prices:
            if cheapest < p:
                diff = max(diff, p - cheapest)
            else:
                cheapest = p
        return diff
=======
		这道题目描述不清，而且没有示例，做的很难受。搞不懂需求
        """
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                maxprofit += prices[i] - prices[i-1]
        return maxprofit
>>>>>>> 8c2a96acf565228030b32c4b18112f8b62303104
