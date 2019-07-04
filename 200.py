class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.helper(grid, i, j)
                    ans += 1
        return ans
    
    # 不知道为什么内联性的helper会超过递归栈
    # 小窍门，改grid从而省去visit
    def helper(self, grid, x, y):
            if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y] != '1':
                return
            grid[x][y] = '#'
            dire = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for i in range(4):
                self.helper(grid, x+dire[i][0], y+dire[i][1])
