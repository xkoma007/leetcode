# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l_map = dict()
        cur_node = head
        while cur_node:
            if cur_node.val not in l_map:
                l_map[cur_node.val] = 1
            else:
                l_map[cur_node.val] += 1
            cur_node = cur_node.next

        new_node = head
        while new_node:
            if l_map[new_node.val] == 1:
                break
            else:
                new_node = new_node.next
        head = new_node
        if not new_node:
            return head
        while new_node.next:
            if l_map[new_node.next.val] > 1:
                new_node.next = new_node.next.next
            else:
                new_node = new_node.next
        return head
