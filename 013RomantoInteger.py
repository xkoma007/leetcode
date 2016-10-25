class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        """
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
        m_len = len(s)
        pos, num = 0, 0

        while pos < m_len:
            if s[pos] in ['I', 'X', 'C']:
                if (pos+1) < m_len and romans[s[pos+1]] > romans[s[pos]]:
                    num += romans[s[pos+1]] - romans[s[pos]]
                    pos += 2
                else:
                    num += romans[s[pos]]
                    pos += 1
            else:
                num += romans[s[pos]]
                pos += 1
        return num

c = Solution()
print(c.romanToInt("MCMXCVI"))
print(c.romanToInt("DCXXI"))
