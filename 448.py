class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in nums:
            idx = abs(i) - 1
            nums[idx] = abs(nums[idx]) * -1
        return [i+1 for i, n in enumerate(nums) if n > 0]
