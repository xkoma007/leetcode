# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small_node, big_node = None, None
        cur_node = head
        while cur_node:
            if cur_node.val >= x:
                big_node = cur_node
                break
            else:
                small_node = cur_node
            cur_node = cur_node.next
        if not big_node:
            return head
        last_node = big_node
        sec_node = last_node.next
        while sec_node:
            if sec_node.val < x:
                if not small_node:
                    small_node = sec_node
                    head = small_node
                    last_node.next = sec_node.next
                else:
                    last_node.next = sec_node.next
                    small_node.next = sec_node
                    small_node = sec_node
                small_node.next = big_node
            else:
                last_node = sec_node
            sec_node = last_node.next
        return head

head = ListNode(2)
cur_node = ListNode(1)
head.next = cur_node
c = Solution()
print(c.partition(head,2))
