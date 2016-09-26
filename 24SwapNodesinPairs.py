# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        m_first = head
        m_second = head.next
        m_swap = m_second.next
        m_first.next = m_swap
        m_second.next = m_first
        head = m_second

        m_before = m_first
        while m_swap is not None and m_swap.next is not None:
            m_first = m_swap
            m_second = m_swap.next
            m_swap = m_second.next
            m_first.next = m_swap
            m_second.next = m_first
            m_before.next = m_second
            m_before = m_first

        return head


def test():
    m_list = ListNode(1)
    m_list2 = ListNode(2)
    m_list3 = ListNode(3)
    m_list4 = ListNode(4)
    m_list.next = m_list2
    m_list2.next = m_list3
    m_list3.next = m_list4

    c = Solution()
    head = c.swapPairs(m_list)
    while head is not None:
        print(head.val)
        head = head.next
test()
