# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from Queue import PriorityQueue  # in py3, use queue
        
        head = p = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
        # in py3, 当第一个值一样的时候，比较第二个值，所以若第二值不支持比较，就会报错。
                q.put((l.val, l))      
        while not q.empty():
            val, node = q.get()
            p.next = node
            p = p.next
            if node.next:
                q.put((node.next.val, node.next))
        
        return head.next
