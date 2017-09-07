#coding=utf-8
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = ''
        i, j = len(a)-1, len(b)-1
        jin = 0
        while i>=0 and j>=0:
            tmp = int(a[i]) + int(b[j]) + jin
            if tmp < 2:
                ans = str(tmp) + ans
                jin = 0
            else:
                jin = 1
                ans = str(tmp-2) + ans
            i -= 1
            j -= 1
        while i >= 0:
            tmp = int(a[i]) + jin
            if tmp < 2:
                ans = str(tmp) + ans
                jin = 0
            else:
                jin = 1
                ans = str(tmp-2) + ans
            i -= 1
        while j >= 0:
            tmp = int(b[j]) + jin
            if tmp< 2:
                ans = str(tmp) + ans
                jin = 0
            else:
                jin = 1
                ans = str(tmp-2) + ans
            j -= 1
        if jin == 1:    ans = '1' + ans     #1 + 1 = 10，这种最后需要额外进位
        return ans

def another(a,b):
    return bin(int(a,2)+int(b,2))[2:]       #one-line solution
#这个很bug，先转成10进制相加，和再转成2进制