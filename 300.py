class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        My solution is not clean. Mix of naive dp and logN
        """
        a, count = list([]), 0
        for num in nums:
            if count==0 or (count and num > a[-1]):
                a.append(num)
                count += 1
            else:
                for i in range(count):
                    if a[i] >= num:
                        a[i] = num
                        break
        return count

    def lengthOfLIS1(self, nums):
        if not nums:
            return 0
        dp,ans = [1]* len(nums),1
        for i in range(1,len(nums)):
            dp[i]=max([dp[j]+1 for j in range(i) if nums[i]>nums[j]]+[1])
            ans=max(ans,dp[i])
        return ans
