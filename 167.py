class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        leng = len(numbers)
        i, j = 0, leng - 1
        while i < j:
            tmp = numbers[i] + numbers[j]
            if tmp == target:
                break
            elif tmp > target:
                j -= 1
            else:
                i += 1
        return i+1, j+1

    # dictionary. Another solution copied from others
    def twoSum2(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            dic[num] = i