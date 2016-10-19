class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        m_curlist = []
        m_lstlist = []
        numRows = rowIndex + 1
        for i in range(numRows):
            for j in range(i + 1):
                if j == 0:
                    m_curlist.append(1)
                elif j == i:
                    m_curlist.append(1)
                else:
                    m_curlist.append(m_lstlist[j-1] + m_lstlist[j])
            m_lstlist = m_curlist
            m_curlist = []
        m_curlist = m_lstlist
        return m_curlist


c= Solution()
print(c.getRow(3))
