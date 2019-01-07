# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 看着简单，写起来还是要考虑很多边界情况的！！！
        if not head:
            return False
        p1, p2 = head, head
        while True:
            if p1.next and p2.next and p2.next.next:
                p2 = p2.next.next
                p1 = p1.next
            else:
                return False
            if p2 == p1:
                return True
        
        # 下面的代码更优雅简洁
        # 另一种处理方式：因为p2在前面，所以判断p2.
        p1,p2 = head,head
        while(p2 and p2.next!=None):
            p1 = p1.next
            p2 = p2.next.next
            if (p1==p2):
                return True
        return False
