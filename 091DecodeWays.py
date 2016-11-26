class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_s = s
        if not new_s or new_s[0] == '0':
            return 0
        m_len = len(new_s)
        m_rels = [0] * m_len
        m_rels[0] = 1

        for pos in range(1, m_len):
            if new_s[pos] != '0':
                m_rels[pos] += m_rels[pos-1]
            two_num = new_s[pos-1] + new_s[pos]
            new_num = int(two_num)
            if new_num >= 10 and new_num <= 26:
                if (pos - 2) >= 0:
                    m_rels[pos] += m_rels[pos-2]
                else:
                    m_rels[pos] += 1
        return m_rels[m_len-1]
c = Solution()
print(c.numDecodings("27"))
