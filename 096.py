class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
		第一反应是卡特兰数，但是也不知道对不对。后面发现卡特兰数的应用真有这个。
		记住公式and 下面分母。
        """
        ans = 1
        for i in range(n+1, 2*n+1):
            ans *= i 
            ans /= (i-n)
        ans /= (n+1)
        return ans
		
	# dp解法难想
class Solution1(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
		下面的解释好懂一些
		Then assume we have the number of the first 4 trees:
		dp[1] = 1 ,dp[2] =2 ,dp[3] = 5, dp[4] =14 , 
		how do we get dp[5] based on these four numbers is the core problem here.
		The essential process is: to build a tree, we need to pick a root node, 
		then we need to know how many possible left sub trees and right sub trees can be held under that node, 
		finally multiply them.
		To build a tree contains {1,2,3,4,5}. 
		First we pick 1 as root, for the left sub tree, there are none; 
		for the right sub tree, we need count how many possible trees are there constructed from {2,3,4,5},
		 apparently it’s the same number as {1,2,3,4}. 
		 So the total number of trees under “1” picked as root is dp[0] * dp[4] = 14. (assume dp[0] =1). 
		 Similarly, root 2 has dp[1]*dp[3] = 5 trees. 
		 root 3 has dp[2]*dp[2] = 4, root 4 has dp[3]*dp[1]= 5 and root 5 has dp[0]*dp[4] = 14. Finally sum the up and it’s done.
        """
        dp = [1] * (n+1)
        for i in range(2, n):
            for j in range(1, i+1):
                dp[i] += dp[i-j] * dp[j-1]
        return dp[n]