class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
		Obviously DP. be careful with setting grid[1,1] = 1.  How to set two dimension array in python
        """
        a = [0] * (n+1)
        grid = [a] * (m+1)
        grid[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[m][n]
	
	"""
	This is a math solution, considering this problem as a permutation. 排列问题：D R R R D R R R
	需要把给定的m、n 减一再计算
	"""	
	public int uniquePaths(int m, int n) {
        if(m == 1 || n == 1)
            return 1;
        m--;
        n--;
        if(m < n) {              // Swap, so that m is the bigger number
            m = m + n;
            n = m - n;
            m = m - n;
        }
        long res = 1;
        int j = 1;
        for(int i = m+1; i <= m+n; i++, j++){       // Instead of taking factorial, keep on multiply & divide
            res *= i;
            res /= j;
        }
            
        return (int)res;
    }
