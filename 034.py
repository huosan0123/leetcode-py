class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        
        up_i, up_j = 0, len(nums)-1
        while up_i < up_j:
            mid = (up_i+up_j) / 2
            if mid == up_i:
                if nums[up_j] != target:
                    up_j = up_i
                else:
                    up_i = up_j
                break
                
            if nums[mid] <= target:
                up_i = mid
            else:
                up_j = mid - 1
        
        lo_i, lo_j = 0, len(nums)-1
        while lo_i < lo_j:
            mid = (lo_i+lo_j) / 2
            if nums[mid] >= target:
                lo_j = mid
            else:
                lo_i = mid + 1
        
        if nums[up_j] == target:
            return [lo_i, up_i]
        else:
            return [-1, -1]
        
