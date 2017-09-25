class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        count = 0         #my method is like C
        for i in word:
            if i.isupper() == True:
                count += 1
        if count == 1:
            if word[0].isupper():
                return True
            else:
                return False
        else:
            if count == len(word) or count == 0:
                return True
            else:
                return False

    def anothor(self, word):
        return word.isupper() or word.islower() or word.istitle()  #very short