#coding=utf-8
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:             #分情况讨论
            ch = str(-x)      #负数变成正数在str
            rch = ch[::-1]     #切片神迹
            n = 0 - int(rch)
        else:
            ch = str(x)
            rch = ch[::-1]
            n = int(rch)
        if n < -2**31 or n > 2**31-1: #32bit sighed integer的上下限
            return 0
        else:
            return n

def reverse(self, x):
    s = cmp(x, 0)
    r = int(`s*x`[::-1])      #convert to abs
    return s*r * (r < 2**31)  #范围内是1，否则是0
