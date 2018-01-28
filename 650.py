class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
		solve it by meself. Time complexity is O(n^2)
        """
        dp = [0] * (n+1)
        for i in range(2, n+1):
            mini = 99999999
            for j in range(1, i):  # exclusive of i
                if i % j == 0:
                    mini = min(mini, dp[j]+i/j)
            dp[i] = mini
        return dp[n]
	
	# this solution is not dp. It's much like math. Convert to n = Prime Factorization. See details on leetcode-solutions
	def minSteps1(self, n):
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans