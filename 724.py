class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalsum = 0
        leftsum = 0
        for n in nums:
            totalsum += n
        for i, n in enumerate(nums):
            rightsum = totalsum - n - leftsum
            if leftsum == rightsum:
                return i
            leftsum += n
        return -1
