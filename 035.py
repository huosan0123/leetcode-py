class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        i, j = 0, n - 1
        mid = 0
        while (i < j):
            mid = (i + j) / 2
            if nums[mid] > target:
                j = mid - 1 
            elif nums[mid] < target:
                i = mid + 1
            else:
                return mid
        
        if nums[i] >= target:
            return i
        else:
            return i+1
