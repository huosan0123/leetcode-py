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
    
    # 不知道为什么内联性的helper会超过递归栈  -> 是我代码写错了
    # 小窍门，改grid从而省去visit
    def helper(self, grid, x, y):
            if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y] != '1':
                return
            grid[x][y] = '#'
            dire = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for i in range(4):
                self.helper(grid, x+dire[i][0], y+dire[i][1])

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        if not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visit = [[0]*n for i in range(m)]
        
        def helper(x, y):
            # 这里除了visit之外没有判断grid为0的地方，导致无穷递归
            if x<0 or x>=m or y<0 or y>= n or visit[x][y] == 1 or grid[x][y]=='0':
                return
            visit[x][y] = 1
            helper(x + 1, y)
            helper(x - 1, y)
            helper(x, y + 1)
            helper(x, y - 1)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visit[i][j] == 0:
                    helper(i,j)
                    ans += 1
        return ans
