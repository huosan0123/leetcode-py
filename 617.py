# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1!=None and t2!=None:
            tmpNode = TreeNode(t1.val + t2.val)
            tmpNode.left = self.mergeTrees(t1.left, t2.left)
            tmpNode.right = self.mergeTrees(t1.right, t2.right)
            return tmpNode
        elif t1!=None:
            tmpNode = TreeNode(t1.val)
            tmpNode.left = self.mergeTrees(t1.left, None)
			#对象里面的递归调用写法。
            tmpNode.right = self.mergeTrees(t1.right, None)
            return tmpNode
        elif t2!=None:
            tmpNode = TreeNode(t2.val)
            tmpNode.left = self.mergeTrees(None, t2.left)
            tmpNode.right = self.mergeTrees(None, t2.right)
            return tmpNode
        else:
            return None
			
def mergeTrees(self, t1, t2):
#很简洁的写法，需要对语法和代码都很了解才行
    if not t1 and not t2: return None
    ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
    ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
    ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
    return ans