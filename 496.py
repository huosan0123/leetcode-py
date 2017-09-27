class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        The description of this problem is diffcult to get. I tried lots of times.
        My solution is not good.
        """
        pos = []
        ans = []
        for i in findNums:       #O(n**2)
            pos.append(nums.index(i))
        for posi in pos:
            flag = 1
            for i in range(posi+1, len(nums)):
                if nums[i]>nums[posi]:
                    ans.append(nums[i])
                    flag = 0
                    break
            if flag:    ans.append(-1)
        return ans

#the following is a O(n) solution using stack.
def anothor(findNums, nums):
    d = {}      #store the dict
    st = []     #stack
    ans = []

    for x in nums:
        while len(st) and st[-1] < x:
            d[st.pop()] = x
        st.append(x)

    for x in findNums:
        ans.append(d.get(x, -1))

    return ans