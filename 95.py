# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # 这里真的是太奇葩了，把start end 换成 l r，代码就会出错。哦哦，懂了
        # 因为下面tree里面我也用了l r。命名重复！！！！
        def dfs(start, end):
            if start > end:
                return [None]
            all_trees = []
            for i in range(start, end+1):
                l_trees = dfs(start, i-1)
                r_trees = dfs(i+1, end)
                
                for l in l_trees:
                    for r in r_trees:
                        p = TreeNode(i)
                        p.left = l
                        p.right = r
                        all_trees.append(p)
            return all_trees
        
        return dfs(1, n) if n else []
