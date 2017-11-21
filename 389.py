class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a, b = [0]*26, [0]*26
        base = ord('a')
        for ch in s:
            a[ord(ch)-base] += 1
        for ch in t:
            b[ord(ch)-base] += 1
        for i in range(26):
            a[i] = b[i] - a[i]
            if a[i] != 0:
                return chr(i+base)
        
		''' one line solution using Counter. counter居然还能 + -
		return list((collections.Counter(t) - collections.Counter(s)))[0]
		'''