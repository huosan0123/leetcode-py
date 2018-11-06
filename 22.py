class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # I know the ituition, but don't know how to code
        ans = []
        
        def dfs(l, r, path, ans):
            if l == 0 and r == 0:
                ans.append(path)
                return
            if r > 0:
                dfs(l, r - 1, path+')', ans)
            if l > 0:
                dfs(l-1, r+1, path+'(', ans)
        
        dfs(n, 0, '', ans)
        return ans
