class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        m_sumlist = []
        m_curlist = []
        for i in range(numRows):
            for j in range(i + 1):
                if j == 0:
                    m_curlist.append(1)
                elif j == i:
                    m_curlist.append(1)
                else:
                    m_curlist.append(m_sumlist[i-1][j-1] + m_sumlist[i-1][j])
            m_sumlist.append(m_curlist)
            m_curlist = []
        return m_sumlist

c = Solution()
print(c.generate(19))
