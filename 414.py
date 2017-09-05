class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set(nums)                                   #directly form a set from list or string
        ans = sorted(a, reverse = True)                  #sorted returns list
        return ans[0] if len(a) < 3   else    ans[2]     # in one line

""" another good solutions
class Solution(object):
    def thirdMax(self, nums):
        v = [float('-inf'), float('-inf'), float('-inf')]   #always keep a list of lenth=3
        for num in nums:
            if num not in v:
                if num > v[0]:   v = [num, v[0], v[1]]      #good idea
                elif num > v[1]: v = [v[0], num, v[1]]
                elif num > v[2]: v = [v[0], v[1], num]
        return max(nums) if float('-inf') in v else v[2]    #if else in one line

class Solution(object):
    def thirdMax(self, nums):
        
        :type nums: List[int]
        :rtype: int
        
        nums = set(nums)
        if len(nums) >= 3:
            nums.remove(max(nums))        #using built-in max and remove method of set
            nums.remove(max(nums))
        return max(nums)
        
"""
