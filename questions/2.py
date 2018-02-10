"""2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their
nodes contain a single digit. Add the two numbers and return it as a
linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        current = result
        carry = 0
        while l1 or l2:
            x1 = l1.val if l1 is not None else 0
            x2 = l2.val if l2 is not None else 0

            sums = x1 + x2 + carry
            carry = 0
            if sums > 9:
                carry = 1
                sums = sums - 10

            current.next = ListNode(sums)
            current = current.next
            l1 = l1 and l1.next
            l2 = l2 and l2.next

        if carry:
            current.next = ListNode(carry)

        return result.next
