class Solution(object):
    m_rel = [0]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = len(Solution.m_rel)
        while m <= n:
            Solution.m_rel.append(m)
            for i in range(1, m+1):
                sq_num = i*i
                if sq_num <= m:
                    Solution.m_rel[m] = min(Solution.m_rel[m], Solution.m_rel[m-sq_num]+1)
                    pass
                else:
                    break
            m += 1
        return Solution.m_rel[n]

c = Solution()
print(c.numSquares(8829))
