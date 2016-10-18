class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 2*5 = 10 , the number 2 is more than the number 5, so we just
        # count the number of 5.

        m_cur = n // 5
        m_count = 0
        while m_cur != 0:
            if m_cur < 0:
                m_cur = -m_cur
            m_count += m_cur
            m_cur = m_cur // 5
            
        return m_count
    def fac(self,n):
        if n == 1 :
            return 1
        return n*self.fac(n-1)

c = Solution()
m_var = 50
print(c.trailingZeroes(m_var))
print(c.fac(m_var))
