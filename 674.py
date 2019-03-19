class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        count, maxcount = 1, 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                if count > maxcount:
                    maxcount = count
                count = 1
        if count > maxcount:
            maxcount = count
        return maxcount
