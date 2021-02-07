# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # https://leetcode-cn.com/problems/reorder-list/
        if not head:
            return

        vec = list()
        cur = head
        while cur:
            vec.append(cur)
            cur = cur.next

        i, j = 0, len(vec)-1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1

        vec[i].next = None

        # 快慢指针找到链表中点，再合并左半端和反转后的右半段即可完成。
