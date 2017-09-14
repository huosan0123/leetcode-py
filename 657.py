class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        a = [0]*256
        for ch in moves:
            a[ord(ch)] += 1
        if (a[ord('L')] == a[ord('R')]) and (a[ord('U')] == a[ord('D')]):
            return True
        else:
            return False
    def another(self, moves):
        return moves.count('L')==moves.count('R') and moves.count('U')==moves.count('D') #using count method of string

    def another1(self, moves):
        from collections import Counter
        a = Counter(moves)
        return a['L']==a['R'] and a['U']==a['D']     #well use of counter. If the dict has no key, return 0