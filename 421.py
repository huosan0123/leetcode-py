class TrieNode():
    def __init__(self):
        self.one = None
        self.zero = None

class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this part build Trie。
        # 加上root，树33层
        root = TrieNode()
        for n in nums:
            node = root
            for i in range(31, -1, -1):
                # 获取每一bit是0 or 1
                tmp = n & (1 << i)
                if tmp:
                    if not node.one:  # 当这个数字的某一位不存在的时候，创建新的节点
                        node.one = TrieNode()
                    node = node.one
                else:
                    if not node.zero:
                        node.zero = TrieNode()
                    node = node.zero
        
        # 按照构建的流程，每个数字会有对应的xor值。
        # 根据数字的bit位，找它的最大的xor值。
        # 注意从root开始，然后才是正确结果。可以按照第一位就不同去考虑
        ans = 0
        for n in nums:
            node, tmp_val = root, 0
            for i in range(31, -1, -1):
                # 当前bit 是 0 or 1
                tmp = n & (1<<i)
                if node.one and node.zero:
                    if tmp:
                        node = node.zero
                    else:
                        node = node.one
                    tmp_val += 1<<i
                else:
                    if (node.one and not tmp) or (node.zero and tmp):
                        tmp_val += 1<<i
                    node = node.one or node.zero
            ans = max(ans, tmp_val)
        return ans
                    
                
        
        
