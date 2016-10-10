class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        m_numAll = 0
        m_chToNums = dict()
        m_initch = 'A'
        for i in range(26):
            m_chToNums[m_initch] = i + 1
            m_initch = chr(ord(m_initch) + 1)
        m_factor = 1
        for ch in s[::-1]:
            m_numAll += m_chToNums[ch] * m_factor
            m_factor *= 26
        return m_numAll

c= Solution()
print(c.titleToNumber("BA"))
