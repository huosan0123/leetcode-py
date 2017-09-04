class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        abc = {}
        for i in range(26):
            abc[i] = chr(ord('A') + i)     #produce a dict, note 0==A
        ans = ''
        while n > 0:
            ans = abc[(n-1) % 26] + ans    #here is different from integer convertion
            n = (n - 1) / 26               #here is different, too
        return ans                         #return ans[::-1] will reverse
