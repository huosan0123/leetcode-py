class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        revs = s[::-1]
        a = revs.split()[::-1]
        return ' '.join(a)