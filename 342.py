#coding=utf-8
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        re = 1
        while re <= num:
            if re == num:
                break
            else:
                re *= 4
        return True if re == num else False

"""
this works, but not so good. The best way is bit manipulation.
4的所有power的二进制表示很有规律，利用此规律解题。充分理解num&(num-1)这一步
"""
def isPowerOfFour(self, num):
        return num != 0 and num &(num-1) == 0 and num & 1431655765== num
