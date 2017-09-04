#coding=utf-8
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans = True
        i, j = 0, len(s) - 1
        while i < j:
            while s[i].isalnum() == False and i < j:    #字符串的方法isalnum
                i += 1
            while s[j].isalnum() == False and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():            #忽略大小写
                ans = False
                break
            else:                     #相同，i向后，j向前
                i += 1
                j -= 1
        return ans
