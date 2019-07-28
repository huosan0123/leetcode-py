# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        from collections import deque
        q = deque()
        q.append(root)
        while q:
            p = q.popleft()
            if p:
                q.append(p.left)
                q.append(p.right)
            else:
                while q:
                    node = q.popleft()
                    if node:
                        return False
        return True
