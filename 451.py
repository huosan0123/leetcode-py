class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for ch in s:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
        pairs = sorted(d.items(), key=lambda item:item[1], reverse=True)
        ans = ''
        for p in pairs:
            ans += p[0] * p[1]
        return ans
