class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        dire1 = [0, 0, 1, -1]
        dire2 = [1, -1, 0, 0]
        m, n = len(image), len(image[0])
        visited = [[0]*n for i in range(m)]
        origin = image[sr][sc]
        
        def helper(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y]==1 or image[x][y]!=origin:
                return
            image[x][y] = newColor
            visited[x][y] = 1
            for i in range(4):
                helper(x+dire1[i], y+dire2[i])
        
        helper(sr, sc)
        return image
 # 理解好题目意思，是把与给node的color连通的同色变成新色
 # 所谓洪水法就是有条件的dfs或者bfs啊
