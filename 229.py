class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        # Note: intialize two candidate with two different values. to prevent [1,1,1,1]
        cA, cB, candiA, candiB = 0, 0, 0, 1  
        
        for n in nums:
            if n == candiA:
                cA += 1
            elif n == candiB:
                cB += 1
            elif cA == 0:
                candiA = n
                cA = 1
            elif cB == 0:
                candiB = n
                cB = 1
            else:
                cA -= 1
                cB -= 1
                
        return [n for n in (candiA, candiB) if (nums.count(n) > len(nums)//3)] 
        
