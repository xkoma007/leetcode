# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        m_len = 0

        curr_list = head
        while curr_list:
            m_len += 1
            curr_list = curr_list.next

        if m_len == 1:
            return None
        if m_len == n:
            return head.next
        # remove m_len-n+1
        curr_list = head
        count = 1
        while count < m_len - n:
            curr_list = curr_list.next
            count += 1

        tmp_list = curr_list.next
        curr_list.next = tmp_list.next
        return head
