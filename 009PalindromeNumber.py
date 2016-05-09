class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        elif x < 0:
            return False
        else:
            m_value = x
        m_list = []
        while m_value != 0:
            m_list.append(m_value % 10)
            m_value = m_value/10
        m_len = len(m_list)
        for i in xrange(m_len/2):
            if m_list[i] != m_list[m_len-1-i]:
                return False
        return True


sol = Solution()
print sol.isPalindrome(-2147447412)
