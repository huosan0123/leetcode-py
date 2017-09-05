#coding=utf-8
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s.count(' ') == len(s): #两种特例
            return 0
        else:
            return len(s.strip().split()[-1]) #string最末的空格去掉
""""
easy to solve. But题目描述不太好，特例需要好好考虑
"""
