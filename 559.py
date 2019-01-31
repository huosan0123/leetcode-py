"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        depths = [self.maxDepth(ch) for ch in root.children]
        # children 使用list表示的，可能为空；
        if not depths:
            depth = 0
        else:
            depth = max(depths)
        return 1 + depth
