# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head
        m_head = head
        while m_head and m_head.val == val:
            m_head = m_head.next

        if m_head is None:
            return None

        m_nextNode = m_head.next
        m_lastNode = m_head
        while m_nextNode:
            if m_nextNode.val == val:
                m_nextNode = m_nextNode.next
                m_lastNode.next = m_nextNode
            else:
                m_lastNode = m_nextNode
                m_nextNode = m_nextNode.next
        return m_head
