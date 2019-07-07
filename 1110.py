# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        if not root or to_delete==[]:
            return root
        delete = set(to_delete)
        ans = []
        self.postorder(root, None, delete, ans)
        return ans
    
    def postorder(self, node, pre, delete, ans):
        if node.val in delete:
            delete.remove(node.val)
            if node.left:
                self.postorder(node.left, None, delete, ans)
            if node.right:
                self.postorder(node.right, None, delete, ans)
        else:
            if pre == None:
                ans.append(node)
            if node.left and node.left.val in delete:
                p = node.left
                node.left = None
                self.postorder(p, None, delete, ans)
            elif node.left:
                self.postorder(node.left, node, delete, ans)
            if node.right and node.right.val in delete:
                p = node.right
                node.right = None
                self.postorder(p, None, delete, ans)
            elif node.right:
                self.postorder(node.right, node, delete, ans)
