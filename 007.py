#coding=utf-8
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:             #���������
            ch = str(-x)      #�������������str
            rch = ch[::-1]     #��Ƭ��
            n = 0 - int(rch)
        else:
            ch = str(x)
            rch = ch[::-1]
            n = int(rch)
        if n < -2**31 or n > 2**31-1: #32bit sighed integer��������
            return 0
        else:
            return n
