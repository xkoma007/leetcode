# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        m_dict = {}
        currnode = head
        befnode = None

        while currnode is not None:
            if currnode.val in m_dict:
                befnode.next = currnode.next
                currnode = currnode.next
            else:
                m_dict[currnode.val] = '1'
                befnode = currnode
                currnode = currnode.next

        return head
