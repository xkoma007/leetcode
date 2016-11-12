# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        cur_node, m_len = head, 0
        while cur_node.next:
            m_len += 1
            cur_node = cur_node.next
        tail = cur_node
        m_len += 1
        k = k % m_len
        n = m_len - k
        cur_node = head
        #  mv (n-1) step
        if k != 0:
            for _ in range(n-1):
                cur_node = cur_node.next
            cur_node.next = None
            tail.next = head
            head = tail
        return head
