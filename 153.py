class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        总共4中情况，然后可以合并的。
        """
        i, j = 0, len(nums)-1
        while i < j:
            mid = (i+j)/2
            if nums[i] < nums[mid] < nums[j]:    # 如果是升序数组
                return nums[i]
            elif nums[j] < nums[mid] < nums[i]:  # 如果是降序数组
                return nums[j]
            elif nums[mid] < nums[j] < nums[i]:  # 正常情况1
                j = mid
            elif nums[mid] > nums[i] > nums[j]:  # 正常情况2
                i = mid
            elif nums[mid] == nums[i] or nums[mid] == nums[j]:  # i j相邻，必为其中之一
                return nums[i] if nums[i] < nums[j] else nums[j]
        return nums[i]

    def findMin(self, nums):
      # 更加concise的写法
        i, j = 0, len(nums)-1
        while i < j-1: # a useful trick
            mid = i + (j-i) / 2
            if nums[mid] < nums[j]:
                j = mid
            else:
                i = mid
        return nums[i] if nums[i] < nums[j] else nums[j]
