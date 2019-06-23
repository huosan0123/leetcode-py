class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.mins = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.st.append(x)
        if not self.mins:
            self.mins.append(x)
        else:
            self.mins.append(min(x, self.mins[-1]))
        

    def pop(self):
        """
        :rtype: None
        """
        if not self.st:
            return
        x = self.st.pop()
        self.mins.pop()
        return x

    def top(self):
        """
        :rtype: int
        """
        if not self.st:
            return
        return self.st[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.st:
            return
        return self.mins[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
