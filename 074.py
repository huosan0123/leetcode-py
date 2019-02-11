class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        把矩阵当作sorted list直接处理。确实符合。
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, m*n-1
        while i < j:
            mid = (i+j) / 2
            if (matrix[mid/n][mid%n] == target):
                return True
            elif matrix[mid/n][mid%n] < target:   # 小于的话，得在该值的下方和右下角找。
                i = mid + 1   # trick，当i j相邻时确保能退出
            else:
                j = mid
        # 最后输出的这里需要判断一下。用i j都行。像[1,3]  3的case就需要出来判断。
        return matrix[j/n][j%n] == target

    def searchMatrix(self, matrix, target):
        """
        剑指 offer上的解法。我自己看了思路也不知道怎么写，无奈
        没想到写出来这么简单，优雅
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j, ans = 0, n-1, False
        while (i<m and j>=0):
            if matrix[i][j] == target:
                ans = True
                break
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return ans
