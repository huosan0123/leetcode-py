# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            p = TreeNode(v)
            p.left = root
            return p
        
        depth_node, depth = {0:[], 1:[root]}, 1
        while depth_node[depth]:
            depth_node[depth+1] = []
            for p in depth_node[depth]:
                if p.left:
                    depth_node[depth+1].append(p.left)
                if p.right:
                    depth_node[depth+1].append(p.right)

            if depth == d-1:  # 我在if内部犯错了，考虑的不够精简
                for p in depth_node[depth]:
                    lp = TreeNode(v)
                    lp.left = p.left
                    p.left = lp
                    rp = TreeNode(v)
                    rp.right = p.right
                    p.right = rp
                break
            depth += 1
                
        return root
