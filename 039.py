class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res
    
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)

# must konw why this answer returns unique solution

# using inner function to avoid parameter sending, a little bit faster.
def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(t, i, path, res):
            if t < 0:
                return
            if t == 0:
                res.append(path)
            for k in range(i, len(candidates)):
                dfs(t-candidates[k], k, path+[candidates[k]], res)
        
        dfs(target, 0, [], res)
        return res
