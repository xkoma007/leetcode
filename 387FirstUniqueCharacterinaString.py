class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        m_rel = -1
        m_fields = dict()

        for ch in s:
            print(ch)
            if ch not in m_fields:
                m_fields[ch] = 1
            else:
                m_fields[ch] += 1

        print(m_fields)
        for m_index, ch in enumerate(s):
            if m_fields[ch] == 1:
                m_rel = m_index
                break

        return m_rel


f = Solution()
print(f.firstUniqChar())
