class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m_rels = [[0] * n for _ in range(m)]
        m_rels[0][0] = 1
        for i in range(m):
            for j in range(n):
                if (i - 1) >= 0:
                    m_rels[i][j] += m_rels[i-1][j]
                if (j - 1) >= 0:
                    m_rels[i][j] += m_rels[i][j-1]
        return m_rels[m-1][n-1]
c = Solution()
print(c.uniquePaths(2, 2))
