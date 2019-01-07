class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if (board == [] or board == [[]]) and not word:
            return True
        m, n = len(board), len(board[0])
        
        #######  这种写法是不对的，因为后面四个dfs调用的时候，如果一个方向False，该路径上的char已被标记为False
        #######  其他方向的调用就会出错。所以正确的答案应该在一个方向出错后，将visit reset，然后返回。
        def dfs(i, j, pos, visit):
            if (i < 0 or i >= m or j <0 or j>=n):
                return False
            if visit[i][j] or board[i][j] != word[pos]:
                return False
            if pos+1 == len(word):
                return True
            
            visit[i][j] = 1
            return dfs(i-1, j, pos+1, visit) or dfs(i+1, j, pos+1, visit) or dfs(i, j-1, pos+1, visit) or dfs(i, j+1, pos+1, visit)
        
        for i in range(m):
            for j in range(n):
                visit = [[0]*n for _ in range(m)]
                if dfs(i, j, 0, visit):
                    return True
        return False
            
    def dfs(i, j, pos):
            if (i < 0 or i >= m or j <0 or j>=n):
                return False
            if board[i][j]=="#" or board[i][j] != word[pos]:
                return False
            if pos+1 == len(word):
                return True
            
            tmp = board[i][j]
            board[i][j] = "#"
            res =  dfs(i-1, j, pos+1) or dfs(i+1, j, pos+1) or dfs(i, j-1, pos+1) or dfs(i, j+1, pos+1)
            board[i][j] = tmp   # 这里直接添加就能返回的啊
            
            return res
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):     # 如果加了visit数组，就会超时。
                    return True
        return False
                      
