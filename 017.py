class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2': "abc", '3':'def', '4':'ghi',
            '5':'jkl', '6':'mno', '7':'pqrs',
            '8':'tuv', '9':'wxyz'}
        ans = []
        if digits == '':
            return ans
        
        def dfs(path, ans, ds):
            if ds == '':
                ans.append(path)
                return
            else:
                for i in d[ds[0]]:
                    dfs(path+i, ans, ds[1:])
        
        dfs('', ans, digits)
        return ans
        
        d = {'2': "abc", '3':'def', '4':'ghi',
            '5':'jkl', '6':'mno', '7':'pqrs',
            '8':'tuv', '9':'wxyz'}
        
        if digits == '':
            return []
        ans = ['']
        for i in digits:
            ans = [s + dig for s in ans for dig in d[i]]             # keep an eye for this grammar!!!
        return ans
