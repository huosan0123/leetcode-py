"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import deque
        deq = deque([root])
        ans = []
        while deq:
            n, level = len(deq), []
            for i in range(n):
                node = deq[i]
                level.append(node.val)
                for child in node.children:     # 这个child的方式
                    deq.append(child)
            
            for i in range(n):
                deq.popleft()
            ans.append(level)
            
        return ans
                    
# 上面代码写的有点啰嗦。
# 不用deque，用tmp_stack 替换 stack，可以更好
