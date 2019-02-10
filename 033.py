class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        自己写的代码虽然很烂，但是速度beats 100. 不知道为何
        """
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        while l < r-1:
            mid = (l+r) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    if target < nums[l]:
                        l = mid
                    else:
                        r = mid
            else:
                if nums[mid] > nums[r]:
                    if nums[mid] > nums[l]:
                        l = mid
                    else:
                        r = mid
                else:
                    if nums[r] < target:
                        r = mid
                    else:
                        l = mid
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1
            
    def search(self, nums, target):
        """
        借鉴别人的代码。速度反而慢了。设计l < r-1是一个trick，可以让r l = mid, 然后跳出while。单独处理l r相邻的情况
        The idea is that when rotating the array, there must be one half of the array that is still in sorted order.
        For example, 6 7 1 2 3 4 5, the order is disrupted from the point between 7 and 1. 
        So when doing binary search, we can make a judgement that which part is ordered and whether the target is in that range, 
        if yes, continue the search in that half, if not continue in the other half.
        """
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        while l < r-1:
            mid = (l+r) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[l]:  #  6,7,0,1,2,3,4,5# 
                if target < nums[mid] or target >= nums[l]:
                    r = mid
                else:
                    l = mid
            else:       # 2,3,4,5,6,7,0,1
                if target > nums[mid] or target < nums[l]:
                    l = mid
                else:
                    r = mid
        
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1
