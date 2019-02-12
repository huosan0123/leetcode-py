class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums)-1
        while i < j:
            mid = (i+j) / 2
            if nums[mid] > nums[mid+1]: # 因为mid < j,所以mid+1不用额外判断
                j = mid
            else:
                i = mid + 1     # 这里每次都是r=mid，left = mid+1。这是一种什么trick
        return i
