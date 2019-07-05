class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, self.dfs(grid, i, j))
        return ans
        
    def dfs(self, grid, x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
            grid[x][y] = '#'
            return self.dfs(grid, x+1, y) + self.dfs(grid, x-1, y) + self.dfs(grid, x, y+1) + self.dfs(grid, x, y-1) + 1
        else:
            return 0
        
