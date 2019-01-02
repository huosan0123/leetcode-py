class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        counter = 0
        while (m != n):
            m >>= 1
            n >>= 1
            counter += 1
        return m << counter
        
  因为是正整数，所以按照题目要求写几个出来瞅瞅。
  要点确实是只要有一位是 0 那么该bit就是0了。
