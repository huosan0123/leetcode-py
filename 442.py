class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in nums:
            idx = abs(i) - 1
            if nums[idx] < 0:
                ans.append(abs(i))
            else:
                nums[idx] = nums[idx] * -1
        return ans
