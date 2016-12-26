class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        if f >=4:
           (f-2)*2 >= f
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        m_rel = 1
        while n > 4:
            n -= 3
            m_rel *= 3

        m_rel *= n
        return m_rel

c = Solution()
print(c.integerBreak(6))
