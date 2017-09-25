class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = bin(num)[2:]
        ans = 0
        for i in a:
            if i == '1':
                ans = ans * 2 + 0
            else:
                ans = ans * 2 + 1
        return ans