# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        path1, path2 = [], []
        
        def preorder(node):
            if node:
                path1.append(node.val)
                preorder(node.left)
                preorder(node.right)
            else:
                path1.append(None)
        
        def postorder(node):
            if node:
                path2.append(node.val)
                postorder(node.right)
                postorder(node.left)
            else:
                path2.append(None)
        
        preorder(root)
        postorder(root)
        return path1 == path2

    另外一个很棒的递归写法！！！别人对于tree的理解就是好，代码也是elegant
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.isMirror(root.left, root.right)
        
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        
        if left.val != right.val:
            return False
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
