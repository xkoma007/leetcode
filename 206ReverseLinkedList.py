# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reverse_node, forward_node, tmp_node = None, head, None
        while forward_node is not None:
            tmp_node = forward_node.next
            forward_node.next = reverse_node
            reverse_node = forward_node
            forward_node = tmp_node

        return reverse_node
