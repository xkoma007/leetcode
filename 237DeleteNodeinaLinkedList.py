# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        ;help: override the cur  node and del the next node
        """
        if not node or not node.next:
            return False

        node.val = node.next.val
        node.next = node.next.next
        return
