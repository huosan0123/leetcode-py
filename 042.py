class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 按照自己的思路连暴力的都不行；所以最关键一步是从找总体洼地 -> 单个元素计算
        # 这是用数组存后半部分最大值的解法
        if len(height)<=2:
            return 0
        n = len(height)
        right = [height[-1]] * n
        for i in range(n-2, -1,-1):
            right[i] = max(height[i], right[i+1])
        
        ans, left = 0, height[0]
        for i in range(1, n):
            left = max(left, height[i])
            ans += min(left, right[i])-height[i]
        return ans
    
    # 双指针，比较难想明白。思路是：
    # 把上面的数组用 两个元素的直接比较代替了
    # i 和 j 位置比较大小；小的那个再和该侧max比看是更新max还是更新
    def trap(self, height):
        if len(height)<=2:
            return 0
        n = len(height)
        i, j = 0, n-1
        left_max, right_max = 0, 0
        ans = 0
        while i < j:
            if height[i] < height[j]:
                if height[i] >= left_max:
                    left_max = height[i]
                else:
                    ans += left_max - height[i]
                i += 1
            else:
                if height[j] >= right_max:
                    right_max = height[j]
                else:
                    ans += right_max - height[j]
                j -= 1
        return ans
