class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ['qwertyuiop','asdfghjkl','zxcvbnm']
        ans = []
        for word in words:
            xrow = 3
            lowword = word.lower()
            for ch in lowword:
                if xrow == 3:
                    for line in rows:
                        if ch in line:
                            xrow = rows.index(line)
                            break
                else:
                    if ch not in rows[xrow]:
                        xrow = 3
                        break
            if xrow != 3:
                ans.append(word)
        return ans
	
	#a short solution using set, well done
	def findwords2(self, words):
		a = set('qwertyuiop')
		b = set('asdfghjkl')
		c = set('zxcvbnm')
		ans = []
		for word in words:
			if a&word == word:
				ans.append(word)
			if c&word == word:
				ans.append(word)
			if b&word == word:
				ans.append(word)
		return ans