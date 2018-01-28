class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
		# My solution consider the cost paid to achieve stair[i], I used another array, more space
        """
        loss = [0] * (len(cost) + 2)
        if len(cost) < 2:
            return 0
        for i in xrange(3, len(cost) + 2):
            loss[i] = min(loss[i-1] + cost[i-2], loss[i-2] + cost[i-3])
        return loss[-1]
        
	def minCostClimbingStairs1(self, cost):
		# Other's solution considers the spending that totally cost at stair[i]
		# only relate with two previous state, so O(n) space
        dp = [0]*(len(cost))
        dp[0], dp[1]=cost[0], cost[1]
        
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-2]+cost[i], dp[i-1]+cost[i])
        
        return min(dp[-2], dp[-1])