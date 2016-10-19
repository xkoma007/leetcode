# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            if l2.val < l1.val:
                m_head = l2
                l2 = l2.next
                m_head.next = l1
                m_curnode = l1
                m_lastnode = m_head
            else:
                m_head = l1
                m_curnode = l1.next
                m_lastnode = m_head

        m_tmpnode = None
        while m_curnode and l2:
            while l2 and l2.val < m_curnode.val:
                m_tmpnode = l2
                l2 = l2.next
                m_lastnode.next = m_tmpnode
                m_tmpnode.next = m_curnode
                m_lastnode = m_tmpnode
            if l2:
                m_lastnode = m_curnode
                m_curnode = m_curnode.next
        if not m_curnode and l2:
            m_lastnode.next = l2
        return m_head
