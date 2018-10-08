class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        a = Counter(nums)
        half = len(nums) / 2
        for key in a:
            if a[key] > half:
                return key
