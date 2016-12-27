# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        tmp_node, count = head, 0
        m_node, n_node = None, None

        while tmp_node:
            count += 1
            if m == count:
                m_node = tmp_node
            if n == count:
                n_node = tmp_node
                break
            tmp_node = tmp_node.next
        if m_node == head:
            bm_node = None
        else:
            bm_node = head
            while bm_node.next != m_node:
                bm_node = bm_node.next
        while m_node != n_node:
            tmp_node = m_node.next
            m_node.next = n_node.next
            n_node.next = m_node
            m_node = tmp_node
        if not bm_node:
            head = n_node
        else:
            bm_node.next = n_node
        return head
