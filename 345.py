#coding=utf-8
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ls = list(s)
        i, j = 0, len(ls) - 1
        while i < j:
            if (ls[i] in dic):
                if ls[j] in dic:
                    tmp = ls[j]
                    ls[j] = ls[i]
                    ls[i] = tmp
                    i += 1
                j -= 1
            else:
                i += 1
        ans = ''
        for ch in ls:
            ans += ch
        return ans             #this should be right but TLE

    def reverseVowels(self, s):  #a very good python solution
        """
        :type s: str           #python don't support change string in-place
        :rtype: str
        """
        import re
        ls = re.findall('[aeiouAEIOU]', s)
        return re.sub('[aeiouAEIOU]', lambda m:ls.pop(), s) #lambada很精髓
