class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        
        def dfs(p, path, ans):
            ans.append(path)
            for i in range(p, len(nums)):
                dfs(i+1, path+[nums[i]], ans)
        
        dfs(0, [], ans)
        return ans
    
    # iteratvie, spend more time
    def answers(self, nums):
        ans = [[]]

            for n in nums:
                ans += [s+[n] for s in ans]
            return ans
