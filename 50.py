class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1.0
        elif n == 1:
            return x
        elif n == -1:
            return 1/x
        else:
            half = self.myPow(x, n//2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
