class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 并不适合backtracking，更像dp
        ans = [0]
        for i in range(n):
            ans.extend([a + 2**i for a in ans[::-1]])
        return ans
