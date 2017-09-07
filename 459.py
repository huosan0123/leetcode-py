#coding=utf-8
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        s1 = (s + s)[1:-1]
        return s1.find(s) != -1

def Another(self, str):
    return str in (2 * str)[1:-1]      #good use of IN operator

"""
如果s是repeat，那么2*s之后肯定是中间还有一个s。如果不是repeated，
2*s之后中间是没有s的
"""