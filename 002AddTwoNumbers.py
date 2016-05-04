class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None    
    
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        m = self.getValueFromList(l1)
        if m < 0:
            return False
        n = self.getValueFromList(l2)
        if n < 0:
            return False
            
        rlist =  self.getListFromValue(m + n)
        return rlist

    def getListFromValue(self, val):
        m_initnode = ListNode(0)
        m_node = m_initnode
        while val/10 != 0:
            m_node.val = val % 10
            val =  val / 10
            m_newnode = ListNode(0)
            m_node.next = m_newnode
            m_node = m_newnode
        m_node.val = val % 10
        m_node.next = None

        return m_initnode

        
    def getValueFromList(self,node):
        nRet, count = 0,0
        nBase = 10
        
        while node.next != None:
            nRet += node.val * (nBase ** count)
            count = count + 1
            node = node.next
        nRet += node.val * (nBase ** count)
        
        return nRet    

# m =  Solution()
# a =  ListNode([2, 4, 3])
# b =  ListNode([5, 6, 4])
# print m.addTwoNumbers(a, b).val
    

    


