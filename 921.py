class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        # my code is not so good
        if S == "":
            return 0
        a = [S[0]]
        for i in S[1:]:
            if i == ')':
                if len(a) > 0 and a[-1] == '(':
                    a.pop()
                else:
                    a.append(')')
            else:
                a.append('(')
        return len(a)
        
        ans = []
        for i in S:
            if i == ")" 
                if len(a) > 0 and a[-1] == '(':
                    a.pop()
                else:
                    a.append("(")
            else:
                a.append('(')
        return len(ans)
                
