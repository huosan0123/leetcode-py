class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.st = []
        self.root = root

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.st or self.root:
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        while self.root:
            self.st.append(self.root)
            self.root = self.root.left
        
        p = self.st.pop()
        self.root = p.right
        return p.val
