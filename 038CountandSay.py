class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        m_str = "1"
        for j in range(1, n):
            m_len = len(m_str)
            start_pos = 0
            m_newlist = []

            while start_pos < m_len:
                if m_str[start_pos] == '2':
                    m_newlist.append("12")
                    start_pos += 1
                elif m_str[start_pos] == '1':
                    if (start_pos + 1 < m_len) and m_str[start_pos + 1] == '1':
                        m_newlist.append("21")
                        start_pos += 2
                    else:
                        m_newlist.append("11")
                        start_pos += 1

            m_str = "".join(m_newlist)

        return m_str


a = Solution()
print a.countAndSay(6)
