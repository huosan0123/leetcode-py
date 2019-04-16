class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        n = len(preorder)
        return self.helper(preorder, inorder, 0, n-1, 0, n-1)
    
    def helper(self, pre, tin, plow, phigh, inlow, inhigh):
        if plow > phigh:
            return None
        if plow == phigh:
            node = TreeNode(pre[plow])
            return node
        root, sep = pre[plow], None
        for i in range(inlow, inhigh+1):
            if tin[i] == root:
                sep = i
                break
        left_len, right_len = sep - inlow, inhigh - sep
        root = TreeNode(root)
        root.left = self.helper(pre, tin, plow+1, plow+left_len, inlow, sep-1)
        root.right = self.helper(pre, tin, plow+left_len+1, phigh, sep+1, inhigh)
        return root
