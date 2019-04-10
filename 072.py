class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1, len2 = len(word1), len(word2)
        
        ans = [[0]*(len2+1) for _ in range(len1+1)]
        for i in range(1, len1+1):
            ans[i][0] = i
        for i in range(1, len2+1):
            ans[0][i] = i
        
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if word1[i-1] == word2[j-1]:
                    ans[i][j] = ans[i-1][j-1]
                else:
                    # 我们可以在k个操作内将 s[1…i] 转换为 t[1…j-1]
                    # 我们可以在k个操作里面将s[1..i-1]转换为t[1..j]
                    # 我们可以在k个步骤里面将 s[1…i-1] 转换为 t [1…j-1]
                    # 针对第1种情况，我们只需要在最后将 t[j] 加上s[1..i]就完成了匹配，这样总共就需要k+1个操作。
                    # 针对第2种情况，我们只需要在最后将s[i]移除，然后再做这k个操作，所以总共需要k+1个操作
                    ans[i][j] = min(ans[i-1][j], ans[i][j-1], ans[i-1][j-1]) + 1
        return ans[len1][len2]
