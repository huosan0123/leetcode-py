class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from heapq import *
        nums = [-x for x in nums]
        heapify(nums)
        while k > 0:            
            x = heappop(nums)   # pop后自动维护堆的性质
            k -= 1
        return -x
       
       
## 重点学习python的heapq的使用方式，data type那部分的数据结构
