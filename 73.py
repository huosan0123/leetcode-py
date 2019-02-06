class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        is_col = False
        for i in range(m):
            if matrix[i][0] == 0:   # 单独处理每行第一个，若有，第一列该0
                is_col = True
            for j in range(1, n):   # 上面单独处理了，所以这里从列的1开始
                if matrix[i][j] == 0:
                    matrix[0][j] = 0 # 列的第一个
                    matrix[i][0] = 0 # 行的第一个
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0  # 如果行首列首有0，则0
        
        # 开始剩余处理第一行和第一列
        # 第一行取决于 【0，0】，第一列取决于is_col
        if matrix[0][0] == 0:
            for i in range(1, n):
                matrix[0][i] = 0
        
        if is_col:
            for i in range(m):   # 这里从0开始一行
                matrix[i][0] = 0
