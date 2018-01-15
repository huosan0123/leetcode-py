class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        This is a naive solution, TLE.
        time complexity: O(n^3)
        """
        chang, ans = len(s), 0
        for i in range(chang):
            tmp_string = ''
            for j in range(i, chang):
                if s[j] not in tmp_string:
                    tmp_string += s[j]
                else:
                    if len(tmp_string) > ans:
                        ans = len(tmp_string)
                    tmp_string = s[j]
            ans = max(ans, len(tmp_string))
        return ans

class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        Another naive solution, TLE.
        time complexity: O(128*128*n), space complexity: O(n)
        """
        chang, ans = len(s), 0
        tmp_string = ""
        for i in range(chang):
            for j in range(i, chang):
                if s[j] not in tmp_string:
                    tmp_string += s[j]
                else:
                    tmp_string = ""
                    break
            if (j - i) > ans:
                ans = j - i
        return ans

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        Accepted solution. In this solution, when s[j] is in the window, move i, but don't move j
        """
        a, ans = {}, 0
        i, j = 0, 0
        while(i < len(s) and j < len(s)):
            if s[j] in a:
                del a[s[i]]  # delete s[i] from dict
                i += 1       # then i slides, while j not move
            else:
                a[s[j]] = 1
                ans = max(ans, j-i+1)   # count the length of substring
                j += 1      # then j slide
        return ans
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        In previous solution, when s[j] is in the window, move i, but don't move j. But, this could be fast.
        Using a map to get position of s[j'] when new s[j] in window, directly move i to that position.
        """
        used_char, ans = {}, 0
        start, j = 0, 0
        for j in range(len(s)):
            if s[j] in used_char and start <= used_char[s[j]]:
                start = used_char[s[j]] + 1        # repeated, should move start to the repeated_position+1
            else:
                ans = max(ans, j - start + 1)
            used_char[s[j]] = j
        return ans

# note the idea of using sliding windows, works well for array and string
