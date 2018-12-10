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
