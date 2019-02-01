class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
	I consider different situations. But the space could be less.
	Notice this problem can't initial with extra colu/row with 0
        """
        N, M = len(grid), len(grid[0])
        path = [[0]*(M) for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if i > 0 and j > 0 :
                    path[i][j] = min(path[i-1][j], path[i][j-1]) + grid[i][j]
                elif i == 0 and j > 0:
                    path[i][j] = path[i][j-1] + grid[i][j]
                elif i > 0 and j == 0:
                    path[i][j] = path[i-1][j] + grid[i][j]
                else:
                    path[i][j] = grid[0][0]
        return path[N-1][M-1] if grid != [[]] else 0
	# using O(1) space
	def minPathSum4(self, grid):
    if not grid:
        return 
    r, c = len(grid), len(grid[0])
    for i in xrange(1, c):
        grid[0][i] += grid[0][i-1]
    for i in xrange(1, r):
        grid[i][0] += grid[i-1][0]
    for i in xrange(1, r):
        for j in xrange(1, c):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1
