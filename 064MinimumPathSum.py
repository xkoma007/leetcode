class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        m_rels = [[0] * n for _ in range(m)]
        m_rels[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0 and j - 1 >= 0:
                    cur_min = min(m_rels[i-1][j], m_rels[i][j-1])
                    m_rels[i][j] = cur_min + grid[i][j]
                elif i - 1 >= 0:
                    m_rels[i][j] = m_rels[i-1][j] + grid[i][j]
                elif j - 1 >= 0:
                    m_rels[i][j] = m_rels[i][j-1] + grid[i][j]
                else:
                    continue
        return m_rels[m-1][n-1]
c = Solution()
print(c.minPathSum([[1]]))
