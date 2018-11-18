class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = []
        
        def dfs(i, path, ans):
            # Note: 满足条件时，最后要return，否则错误。
            if i == len(S) and len(path) == len(S):
                ans.append(path)
                return
            if S[i].isalpha():
                dfs(i+1, path + S[i].lower(), ans)
                dfs(i+1, path + S[i].upper(), ans)
            else:
                dfs(i+1, path + S[i], ans)
        
        dfs(0, "", ans)
        return ans

    # iterative version
    def letterCasePermutation(self, S):
            res = ['']
            for ch in S:
                if ch.isalpha():
                    res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
                else:
                    res = [i+ch for i in res]
            return res
