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

#  this is another similiar solution, also good
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        curr = root
        while curr is not None:
            self.stack.append(curr)
            curr = curr.left
            
    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.stack)

    def next(self):
        """
        :rtype: int
        """
        curr = self.stack.pop()
        val = curr.val
        if curr.right:
            curr = curr.right
            while curr:
                self.stack.append(curr)
                curr = curr.left
        return val
