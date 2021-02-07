# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # https://leetcode-cn.com/problems/linked-list-cycle-ii/

        hashMap = dict()
        # while head:
        #     if head not in hashMap:
        #         hashMap[head] = 1
        #     else:
        #         return head
        #     head = head.next

        slow, fast = head, head
        while fast and slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return slow
        return None