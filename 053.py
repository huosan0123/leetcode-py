# To calculate sum(0,i), you have 2 choices: 
# either adding sum(0,i-1) to a[i], or not. 
# If sum(0,i-1) is negative, adding it to a[i] will only make a smaller sum, so we add only if it's non-negative.
# sum(0,i) = a[i] + (sum(0,i-1) < 0 ? 0 : sum(0,i-1))

public int maxSubArray(int[] nums) {
	if (nums == null || nums.length == 0) { return 0; }
	int max = nums[0], sum = nums[0];
	for (int i = 1; i < nums.length; i++) {
		if (sum < 0) { sum = nums[i]; }
		else {sum += nums[i]; }
		max = Math.max(max, sum);
	}
	return max;
}

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi, tmp_sum = -999999999, 0
        for n in nums:
            if tmp_sum + n >= 0:
                tmp_sum += n
            else:
                tmp_sum = 0
            if tmp_sum > maxi: maxi = tmp_sum
        return max(nums) if maxi==0 else maxi