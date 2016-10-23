import gc


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a_len, b_len = 0, 0
        a_node, b_node = headA, headB

        while a_node:
            a_len += 1
            a_node = a_node.next

        while b_node:
            b_len += 1
            b_node = b_node.next

        a_node, b_node = headA, headB
        m_step = a_len - b_len
        m_count = 0
        if m_step > 0:
            while m_count < m_step:
                a_node = a_node.next
                m_count += 1
        else:
            m_step = -m_step
            while m_count < m_step:
                b_node = b_node.next
                m_count += 1

        while a_node:
            if a_node is b_node:
                gc.collect()
                return a_node
            a_node = a_node.next
            b_node = b_node.next
        gc.collect()
        return None
