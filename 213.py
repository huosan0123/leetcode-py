class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        # 分解之后，就是House Rob的easy题目。
        res1 = self.rob_easy(nums[1:])
        res2 = self.rob_easy(nums[:-1])
        return max(res1, res2)
    
    def rob_easy(self, nums):
        # easy的正确解决也得是dp的。
        # 因为主函数保证了nums肯定有值，所以不必判空。并且下面代码将==2的整合到一起了
        res = [0] * len(nums)
        res[0], res[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            res[i] = max(res[i-1], res[i-2] + nums[i])
            
        return res[-1]
        
        
