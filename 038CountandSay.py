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
                m_num = m_str[start_pos]
                count = 1
                # check the same number count
                while start_pos < m_len:
                    if start_pos + 1 < m_len:
                        if m_str[start_pos + 1] == m_str[start_pos]:
                            start_pos += 1
                            count += 1
                        else:
                            break
                    else:
                        break
                m_value = str(count) + m_num
                m_newlist.append(m_value)
                start_pos += 1
            m_str = "".join(m_newlist)

        return m_str


a = Solution()
print a.countAndSay(4)
