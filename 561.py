class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()     #sort是原地使用的，没有返回值
        return sum(nums[::2])   #这种切片很重要
        