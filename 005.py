class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        oh, my dear. AC in one submit!
        happy for my idea!
        """
        leng = len(s)
        low, high = 0, 0
        for i in range(leng):
            j = 0
            while(i+j<leng and i-j>=0 and s[i-j] == s[i+j]):
                j += 1
            if (2*j-1 > high-low+1):
                high = i+j-1
                low = i-j+1
            if (i+1<leng and s[i] == s[i+1]):
                j = 0
                while (i+1+j < leng and i-j>=0 and s[i-j]==s[i+1+j]):
                    j += 1
                if (2*j > high-low+1):
                    high = i+j
                    low = i-j+1
        return s[low:high+1]
