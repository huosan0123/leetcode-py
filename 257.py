class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        self.preorder(root, [], ans)
        res = ["->".join(path) for path in ans]
        return res
    
    def preorder(self, node, tmp, ans):
        if node:
            tmp.append(str(node.val))
            if node.left is None and node.right is None:
                ans.append(tmp[::])
            if node.left:
                self.preorder(node.left, tmp, ans)
            if node.right:
                self.preorder(node.right, tmp, ans)
            tmp.pop()
