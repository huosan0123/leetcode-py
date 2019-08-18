class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = 0
        ans = 0
        # 即使理解了方法，但是各种边界条件依然很难处理
        # 下面的if 嵌套和l = max(r, l+1)防止了多种情况的死循环
        # 开头是降序；最后一个数字无法跳出等问题。如果在外面找到上升的，但是后面会有==的值,也很麻烦
        # 所以单独在外面处理不行，还是得放到while 里面
        while l < len(A):     
            r = l
            if r+1 < len(A) and A[r] < A[r+1]:
                while r+1 < len(A) and A[r] < A[r+1]:
                    r += 1
                if r+1 < len(A) and A[r] > A[r+1]:
                    while r+1 < len(A) and A[r] > A[r+1]:
                        r += 1
                    if r - l + 1 > ans:
                        ans = r - l + 1
            l = max(r, l+1)
        return ans
            
