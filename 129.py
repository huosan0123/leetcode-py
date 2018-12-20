class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        ans = []
        def dfs(node, path):
            if node:
                path.append(node.val)
                if not node.left  and not node.right:
                    strpath = [str(i) for i in path]
                    val = int("".join(strpath))
                    ans.append(val)
                if node.left:
                    dfs(node.left, path)
                if node.right:
                    dfs(node.right, path)
                path.pop()
        dfs(root, [])
        return sum(ans)
