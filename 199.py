class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if not root:
            return []
        self.post(root, 1, ans)
        return ans
    
    def post(self, node, depth, ans):
        if node is None:
            return
        if len(ans) < depth:
            ans.append(node.val)
        if node.right:
            self.post(node.right, depth+1, ans)
        if node.left:
            self.post(node.left, depth+1, ans)

    def rightSideView(self, root):
        """
        这种解法符合我的思想，当时我不知道如何实现。
        看了别人代码和知道了deque之后，会的
        """
        if root is None:
            return []
        
        from collections import deque
        de = deque()
        de.append(root)
        ans = []
        while de:
            ans.append(de[-1].val)
            for i in range(len(de)):
                p = de.popleft()
                if p.left:
                    de.append(p.left)
                if p.right:
                    de.append(p.right)
        return ans
        
