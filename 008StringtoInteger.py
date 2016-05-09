class Solution(object):
    def wrapBlank(self, str):
        for i in xrange(len(str)):
            if str[i] != ' ':
                return str[i:]
        return str

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0

        m_newstr = self.wrapBlank(str)

        m_negative = False
        if m_newstr[0] == '+':
            m_newstr = m_newstr[1:]
        elif m_newstr[0] == '-':
            m_newstr = m_newstr[1:]
            m_negative = True
        else:
            pass

        m_strnum = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        for i in xrange(len(m_newstr)):
            ch = m_newstr[i]
            if ch not in m_strnum:
                m_newstr = m_newstr[:i]
                break

        m_rel = 0
        m_base = 10
        m_count = 0
        m_len = len(m_newstr)
        for i in xrange(m_len):
            ch = m_newstr[m_len-i-1]
            m_rel += int(ch) * (m_base ** m_count)
            m_count += 1

        if m_negative:
            if m_rel > (2 ** 31):
                return -2**31
            m_rel = 0 - m_rel
        else:
            if m_rel > ((2 ** 31) - 1):
                return (2**31)-1

        return m_rel

a = Solution()
