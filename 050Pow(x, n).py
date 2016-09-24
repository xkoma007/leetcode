class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if  n == 0:
            return 1
        elif n < 0:
            m_positve = False
            n = -n
        else:
            m_positve = True
        
        m_curr = dict()
        m_path = []
        m = n
        while m != 0:
            m_path.append(m)
            m = m//2
        m_path .reverse()

        for i in m_path:
            if i == 1:
                m_curr[i] = x
            else:
                if i %2 == 0:
                    m_curr[i] = m_curr[i//2] * m_curr[i//2]
                else:
                    m_curr[i] = m_curr[i//2] * m_curr[i//2]*x

        if m_positve:
            return m_curr[n] 
        else:
            return 1/m_curr[n]
            

        
f = Solution()
print(f.myPow(34.00515,-3))

            
