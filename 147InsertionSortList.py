# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        sort_head, sort_tail = head, head
        cur_node = head.next
        while cur_node is not None:
            last_node, tmp_node = None, sort_head
            while (cur_node.val > tmp_node.val) and tmp_node is not sort_tail:
                last_node = tmp_node
                tmp_node = tmp_node.next
            if cur_node.val <= tmp_node.val:
                sort_tail.next = cur_node.next
                if not last_node:
                    cur_node.next = sort_head
                    sort_head = cur_node
                else:
                    last_node.next = cur_node
                    cur_node.next = tmp_node
            else:               # tmp_node is sort_tail
                sort_tail = cur_node
            cur_node = sort_tail.next
        return sort_head
