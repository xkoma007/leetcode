class Solution(object):
    def convert_to_list(self, s, numRows):
        new_rels = [[] for _ in range(numRows)]
        vertical_status = True
        m_len, m_pos = len(s), 0
        while True:
            if vertical_status:
                for i in range(numRows):
                    if m_pos < m_len:
                        new_rels[i].append(s[m_pos])
                        m_pos += 1
                    else:
                        return new_rels
                vertical_status = False
            else:
                for i in range(numRows-2, 0, -1):
                    if m_pos < m_len:
                        new_rels[i].append(s[m_pos])
                        m_pos += 1
                    else:
                        return new_rels
                vertical_status = True
        return new_rels

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        new_rels = self.convert_to_list(s, numRows)
        new_s = ""
        for cur_rel in new_rels:
            for cur_ch in cur_rel:
                new_s += cur_ch
        return new_s

c = Solution()
print(c.convert("PAYPALISHIRING", 3))
print(c.convert("A", 1))
print(c.convert("ABCDE", 4))
