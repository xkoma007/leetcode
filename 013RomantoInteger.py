class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'D': 500, 'M': 1000}
        m_len = len(s)
        number = 0

        startPos = 0
        while startPos < m_len:
            # duplicate number
            i = 0
            while i < 3:
                if startPos + 1 >= m_len:
                    break
                elif s[startPos] != s[startPos + 1]:
                    number += roman_nums[s[startPos]]
                    startPos += 1
                    break
                else:
                    number += roman_nums[s[startPos]]
                    startPos += 1
                    i += 1
