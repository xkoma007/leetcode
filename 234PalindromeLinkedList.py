# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        if fast.next:
            # even link list
            slow = slow.next
        # reverse  the last half part of link list
        p, fast = slow, head
        slow = slow.next
        p.next = None
        while slow:
            q = slow.next
            slow.next = p
            p = slow
            slow = q
        # compare
        while p:
            if p.val != fast.val:
                return False
            p = p.next
            fast = fast.next
        return True
