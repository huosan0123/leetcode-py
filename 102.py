class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        from collections import deque
        de = deque()
        de.append(root)
        while de:
            tmp, l = [], len(de)
            for p in list(de):
                tmp.append(p.val)
                if p.left:
                    de.append(p.left)
                if p.right:
                    de.append(p.right)
            while l>0:
                de.popleft()
                l -= 1
            ans.append(tmp)
        return ans
