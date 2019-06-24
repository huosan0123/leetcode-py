class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
        st, n = [0], len(s)
        for i in range(1, n):
            if s[i] == '(':
                st.append(i)
            else:
                if st and s[st[-1]] == '(':
                    st.pop()
                else:
                    st.append(i)
        if st == []:
            return n
        if st[0] > 0:
            ans = st[0]
        else:
            ans = 0
        for i in range(1, len(st)):
            ans = max(st[i]-st[i-1] - 1, ans)
        if st[-1] < n:
            ans = max(n-1 - st[-1], ans)
        return ans
