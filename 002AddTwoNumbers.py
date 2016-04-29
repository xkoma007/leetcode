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

    def getListFromValue(self, value):
        m_list =  ListNode([])
        while value/10 != 0:
            m_list.append(value % 10)
            value =  value / 10
        m_list.append(value % 10)
        return m_list
        
    def getValueFromList(self,linklist):
        nRet ,count = 0,0
        nBase = 10
        for n in xrange(len(linklist)):
            nRet += linklist[n] * (nBase ** count)
            count = count + 1
            
        return nRet    

m =  Solution()
a =  ListNode([1, 8])
b =  ListNode([0])
print m.addTwoNumbers(a, b)
    

    


