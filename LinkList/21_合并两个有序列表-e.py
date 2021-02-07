# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
#         https://leetcode-cn.com/problems/merge-two-sorted-lists/
        head = ListNode()
        cur = head
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next

        while l1 is not None:
            cur.next = l1
            l1 = l1.next
            cur = cur.next

        while l2 is not None:
            cur.next = l2
            l2 = l2.next
            cur = cur.next

        return head

        # 递归策略
        # if l1 and l2:
        #     if l1.val > l2.val:
        #         l1, l2 = l2, l1
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        # return l1 or l2
