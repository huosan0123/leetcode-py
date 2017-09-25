class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = {}
        for item in nums:
            if item not in ans:
                ans[item] = 1
            else:
                ans[item] += 1
        for item in ans:          #dict's operation
            if ans[item] == 1:
                return item