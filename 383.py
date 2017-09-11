class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letters = [0] * 256
        for ch in magazine:
            letters[ord(ch)] += 1
        for ch in ransomNote:
            letters[ord(ch)] -= 1
        for i in range(256):
            if letters[i] < 0:
                return False
        return True

##using built-in module, quite pythonic!!
    def canConstruct1(self, ransomNote, magazine):
        return not collections.Counter(ransomNote) - collections.Counter(magazine)