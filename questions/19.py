"""19. Remove Nth Node From End of List
Given a linked list, remove the nth node from the end of list and
return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list
   becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head

        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head

        while(first is not None):
            length += 1
            first = first.next

        length -= n
        first = dummy
        while (length > 0):
            length -= 1
            first = first.next

        first.next = first.next.next

        return dummy.next