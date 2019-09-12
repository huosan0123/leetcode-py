class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return []
        n = len(ratings)
        ans = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                ans[i] = ans[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                ans[i] = max(ans[i], ans[i+1] + 1)
        return sum(ans)
