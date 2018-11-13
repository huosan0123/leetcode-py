class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        nums.sort()
        
        count, i = 0, 0
        while i < len(nums):
            while i + count < len(nums) and nums[i] == nums[count+i]:
                count += 1
            
            # there'are to ways to add.
            for k in range(len(ans)):
                tmp = ans[k][::]
                for j in range(count):
                    tmp.append(nums[i])
                    ans.append(tmp[::])   # must use copy or store reference
            
            i += count
            count = 0   # reset count to 0
            
        return ans
        
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        nums.sort()
        
        count, i = 0, 0
        while i < len(nums):
            # this count setting is brilliant.
            while i + count < len(nums) and nums[i] == nums[i + count]:
                count += 1
            
            # the 2nd way to do append, this way is slower, why?
            pre_n = len(ans)
            for j in range(1, count+1):
                for k in range(pre_n):
                    ans.append(ans[k]+[nums[i]]*j)
            i += count
            count = 0
            
            i += count
            count = 0
            
        return ans
