class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        m_rel = [0] * (n+1)
        for i in range(1, n+1):
            m_rel[i] = i
            for j in range(1, i+1):
                sq_num = j*j
                if sq_num <= i:
                    m_rel[i] = min(m_rel[i], m_rel[i-sq_num]+1)
                else:
                    break
        return m_rel[n]

c = Solution()
print(c.numSquares(9732))
