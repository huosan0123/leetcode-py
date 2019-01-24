# 自己写的代码贼丑

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        elif (not s and t) or (s and not t):
            return False
        
        def preorder(sn, tn, candidates):
            if sn:
                if sn.val == tn.val:
                    candidates.append(sn)
                preorder(sn.left, tn, candidates)
                preorder(sn.right, tn, candidates)
        candidates = []
        preorder(s, t, candidates)
        print([i.val for i in candidates])
        for sn in candidates:
            if self.test(sn, t):
                return True
        return False
        
    def test(self, sn, tn):
        if not sn and not tn:
            return True
        elif (not sn and tn) or (sn and not tn):
            return False
        else:
            if sn.val != tn.val:
                return False
            return self.test(sn.left, tn.left) and self.test(sn.right, tn.right)
