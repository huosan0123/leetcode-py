class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, count = 1, 0
        while i <= n:
            if i & n:
                count += 1
            i <<= 1
        return count
       
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, count = n-1, 0
        while n:
            n = n & (n-1)
            count += 1
        return count
