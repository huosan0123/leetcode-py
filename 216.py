class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 3 and n > 27:
            return []
        
        ans, path = [], []
        def dfs(k, n, ans, path):
            if k == 0 and n == 0:
                ans.append(path)
            if k < 0 or n < 0:
                return
            if k > 0 and n > 0:
                for i in range(1, 10):
                    if not path:
                        dfs(k-1, n-i, ans, path+[i])
                    elif path and path[-1] < i:
                        dfs(k-1, n-i, ans, path+[i])
        dfs(k, n, ans, path)
        return ans
