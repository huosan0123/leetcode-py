class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
		In order to make the code simple, I used a not so good solution
		dp[i] = max(dp[i-1], dp[i-1] + count*num)
        """
        count = [0] * 10001
        for i, num in enumerate(nums):
            count[num] += 1
        m, n = 0, count[1]  # Good initialization makes code simple
        for i in range(2, 10001):
            tmp = max(n, m + i * count[i])
            m, n = n, tmp
        return n