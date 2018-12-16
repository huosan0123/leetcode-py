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
