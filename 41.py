class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        https://leetcode.windliang.cc/leetCode-41-First-Missing-Positive.html
        """
        # this solution beats 100%, using o(n) space beats 5%.
        # use o(n) space to have better idea
        leng = len(nums)
        for i in range(len(nums)):
            if nums[i]-1 == i:
                continue
            while nums[i] > 0 and nums[i] <= leng and nums[i] != nums[nums[i]-1]:
                tmp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[tmp-1] = tmp      # can't use nums[nums[i]-1]=tmp,因为nums[i]改变了
        
        for i, n in enumerate(nums):
            if n-1 != i:
                return i+1
        return leng+1
