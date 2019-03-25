# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            lh = self.getHeight(root.left)
            rh = self.getHeight(root.right)
            if abs(lh - rh) > 1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def getHeight(self, root):
        if not root:
            return 0
        else:
            left_h = self.getHeight(root.left)
            right_h = self.getHeight(root.right)
            return max(left_h, right_h) + 1

链接：https://www.nowcoder.com/questionTerminal/8b3b95850edb4115918ecebdf1b4d222
来源：牛客网
# 上面的解法同一个节点遍历太多次，这个解法很棒，剪枝
public class Solution {
    public boolean IsBalanced_Solution(TreeNode root) {
        return getDepth(root) != -1;
    }
     
    private int getDepth(TreeNode root) {
        if (root == null) return 0;
        int left = getDepth(root.left);
        if (left == -1) return -1;
        int right = getDepth(root.right);
        if (right == -1) return -1;
        return Math.abs(left - right) > 1 ? -1 : 1 + Math.max(left, right);
    }
}
