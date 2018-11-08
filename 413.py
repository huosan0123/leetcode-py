class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        slices = []
        pre_diff, n = A[1] - A[0], 2
        for i in range(2, len(A)):
            if A[i] - A[i-1] == pre_diff:
                n += 1
            else:
                if n >= 3:
                    slices.append(n)
                pre_diff = A[i] - A[i-1]
                n = 2
        if n >= 3:
            slices.append(n)
        ans = 0
        for p in slices:
            ans += (p-2) * (p-1) / 2
        return ans
 
 # I didn't think out dp solution. My solution is math-based
      opt, i = [0,0], 1
      for j in xrange(2,len(A)):
          if A[j]-A[j-1] == A[j-1]-A[j-2]:
              opt.append(opt[j-1]+i)
              i += 1
          else:
              opt.append(opt[j-1])
              i = 1
      return opt[-1]
