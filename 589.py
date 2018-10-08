"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans, stk = [], []
        stk.append(root)
        while stk:
            p = stk.pop()
            if p:
                ans.append(p.val)
                for i in p.children[::-1]:
                    stk.append(i)
        return ans
