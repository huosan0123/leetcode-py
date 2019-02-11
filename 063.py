class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ans = [[1] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                for j in range(i, m):
                    ans[j][0] = 0
                break
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                for j in range(i, n):
                    
                    ans[0][j] = 0
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    ans[i][j] = 0
                else:
                    ans[i][j] = ans[i-1][j] + ans[i][j-1]
        return ans[m-1][n-1]
