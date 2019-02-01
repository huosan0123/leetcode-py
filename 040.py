class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def dfs(t, i, path, res):
            if t < 0:
                return
            if t == 0:
                res.append(path)
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                dfs(t-candidates[j], j+1, path+[candidates[j]], res)

        dfs(target, 0, [], res)
        return res



# this solution don't pass, get [[],[]]. weird!
class Solution(object):
    def combinationSum2(self, candidates, target):
        """ 
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def dfs(t, cur, path):
            if t == 0:
                res.append(path)
                return
            for j in range(cur, len(candidates)):
                if candidates[j] > t: break
                if j > cur and candidates[j] == candidates[j-1]:
                    continue
                path.append(candidates[j])
                dfs(t-candidates[j], j+1, path)
                path.pop()
        dfs(target, 0, []) 
        return res
