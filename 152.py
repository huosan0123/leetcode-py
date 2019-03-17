class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        maxpre, minpre = nums[0], nums[0]
        for i in range(1, len(nums)):
            maxhere = max(max(maxpre*nums[i], minpre*nums[i]), nums[i])
            minhere = min(min(maxpre*nums[i], minpre*nums[i]), nums[i])
            ans = max(ans, maxhere)
            maxpre = maxhere
            minpre = minhere
        return ans
