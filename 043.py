class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        
        tmps = []
        for n  in num1[::-1]:
            tmp, jin = '', 0
            for m in num2[::-1]:
                t = int(n) * int(m) + jin
                jin, ci = divmod(t, 10)
                tmp = str(ci) + tmp
            if jin > 0:
                tmp = str(jin) + tmp
            tmps.append(tmp)

        part_ji = [int(tmps[i] + '0'*i) for i in range(len(tmps))]
        ans = sum(part_ji)
        
        
        return str(ans)
           
