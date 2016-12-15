class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev_str = ""
        pos = len(s) - 1

        while pos >= 0:
            while pos >= 0 and s[pos] == ' ':
                pos -= 1
            if (pos+1) < len(s) and s[pos+1] == ' ':
                rev_str += ' '
            if pos < 0:
                break
            tmp_str = ""
            while pos >= 0 and s[pos] != ' ':
                tmp_str = s[pos] + tmp_str
                pos -= 1
            rev_str += tmp_str
            if pos < 0:
                break

        m_len = len(rev_str)
        if not m_len:
            return ""
        m_start, m_end = 0, m_len
        if rev_str[0] == ' ':
            m_start = 1
        if rev_str[m_len-1] == ' ':
            m_end = m_len - 1
        return rev_str[m_start: m_end]

c = Solution()
print(c.reverseWords( "  abc       df a    "))
