class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        from collections import Counter
        lens = len(nums)
        if k <= 0:
             return False
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i-dic[v] <= k:
                return True
            dic[v] = i
        return False
