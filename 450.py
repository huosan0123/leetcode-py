# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # 真的很需要综合考虑的思维。完全不会写。
        if not root:
            return
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # 如果左子树空，直接把右子树接上来。如果root.right=None也ok
            if not root.left:
                return root.right
            else:
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right
                # 交换二者的val，然后去删除这个新的val
                root.val = tmp.val
                root.left = self.deleteNode(root.left, tmp.val)
        
        return root
                
                
            
