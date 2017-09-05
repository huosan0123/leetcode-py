#coding=utf-8

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lenth = len(nums)
        b = []
        for i in range(lenth-k, lenth):
            b.append(nums[i])
        for i in range(lenth-k):
            b.append(nums[i])
        for i in range(lenth):
            nums[i] = b[i]
"""i have used a extra list, not so good. I have came up with a solution which reverse
three times, but I find it may need bo write another func. But, list object has
reverse method in python. 23333333333333. 活到老学到老，哈哈

"""
