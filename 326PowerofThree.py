class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        m_init = 1
        while n > m_init:
            m_init *= 3

        if n == m_init:
            return True
        else:
            return False
