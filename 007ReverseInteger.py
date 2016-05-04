class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        m_stack = []

        if x < 0:
            m_current = 0 - x
        else:
            m_current = x
            
        while m_current / 10 !=  0:
            m_stack.append(m_current % 10)
            m_current = m_current / 10
        m_stack.append(m_current % 10)

        m_count = 0
        m_base = 10
        m_rel = 0
        while len(m_stack) != 0:
            m_val = m_stack.pop()
            m_rel += m_val * (m_base ** m_count)
            m_count += 1

        if m_rel > ((2 ** 31) - 1):
            return  0
            
        if x < 0:
            m_rel = 0 - m_rel
        return m_rel

        
            
a = Solution()
print a.reverse( - 123)
print a.reverse(321)            
print a.reverse(0)
print a.reverse(1534236469)
