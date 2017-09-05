#coding=utf-8
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        from math import sqrt
        max = int(sqrt(c))
        i, j = 0, max
        ans = False
        while i <= j:              #退出的条件：72 = 36 + 36
            tmp = i**2 + j**2
            if tmp == c:
                ans = True
                break
            elif tmp < c:
                i += 1
            else:
                j -= 1
        return ans

"""
类似第三种解法
"""

