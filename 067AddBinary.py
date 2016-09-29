class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a_len = len(a)
        b_len = len(b)

        m_interval = a_len - b_len
        if m_interval > 0:
            for _ in range(m_interval):
                b = '0' + b
        elif m_interval < 0:
            for _ in range(-m_interval):
                a = '0' + a
        else:
            pass

        m_currLen = len(a) - 1
        m_carry = 0
        m_currRel = ''
        for _ in range(m_currLen + 1):
            m_currVal = m_carry + int(a[m_currLen]) + int(b[m_currLen])
            if m_currVal == 3:
                m_carry = 1
                m_currRel = '1' + m_currRel
            elif m_currVal == 2:
                m_carry = 1
                m_currRel = '0' + m_currRel
            elif m_currVal == 1:
                m_carry = 0
                m_currRel = '1' + m_currRel
            else:
                m_carry = 0
                m_currRel = '0' + m_currRel
            m_currLen -= 1
        if m_carry == 1:
            m_currRel = '1' + m_currRel

        return m_currRel


c = Solution()
print (c.addBinary("1111","1111"))
