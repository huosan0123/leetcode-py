class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle or not triangle[0]:
            return 0
        ans = [[0 for _ in row] for row in triangle]
        ans[0][0] = triangle[0][0]
        
        for i in range(1, len(triangle)):
            n = len(triangle[i])
            for j in range(n):
                if j == 0:
                    ans[i][j] = ans[i-1][0] + triangle[i][0]
                elif j == n -1:
                    ans[i][-1] = ans[i-1][-1] + triangle[i][-1]
                else:
                    ans[i][j] = min(ans[i-1][j-1], ans[i-1][j]) + triangle[i][j]
                    
        return min(ans[-1])
        
        # 我这个是从上往下，需要o(n*n)的空间
        # 因为是path，还可以从下往上做路径，只需要o(n)的空间
