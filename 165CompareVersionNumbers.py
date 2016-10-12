class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        m_vseq1 = version1.split('.')
        m_vseq2 = version2.split('.')

        m_vlen1 = len(m_vseq1)
        m_vlen2 = len(m_vseq2)
        if m_vlen1 <= m_vlen2:
            m_shortlen = m_vlen1
        else:
            m_shortlen = m_vlen2

        for pos in range(m_shortlen):
            if int(m_vseq1[pos]) > int(m_vseq2[pos]):
                return 1
            elif int(m_vseq1[pos]) < int(m_vseq2[pos]):
                return -1
            else:
                continue
        if m_vlen1 > m_vlen2:
            m_leftseq = m_vseq1
        elif m_vlen1 < m_vlen2:
            m_leftseq = m_vseq2
        else:
            return 0

        for m_val in m_leftseq[m_shortlen:]:
            if int(m_val) > 0:
                if m_vlen1 > m_vlen2:
                    return 1
                else:
                    return -1
        return 0

c = Solution()
print(c.compareVersion("1.0", "1"))
