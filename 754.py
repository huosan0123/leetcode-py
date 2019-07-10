class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        # not easy, copied. math
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
            
        if target == 0 or abs(target)%2 == 0:
            return k
        if (abs(target)+k+1) % 2 == 0:
            return k+1
        else:
            return k+2
