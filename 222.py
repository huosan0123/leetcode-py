class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        lp, rp = root, root
        lh, rh = 0, 0
        while lp:
            lh += 1
            lp = lp.left
        while rp:
            rh += 1
            rp = rp.right
        if lh == rh:
            return 2**lh - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
