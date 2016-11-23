class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n, m = len(obstacleGrid[0]), len(obstacleGrid)
        m_rels = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
            m_rels[0][0] = 1

        m_rels[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i >= 1 and obstacleGrid[i-1][j] != 1:
                    m_rels[i][j] += m_rels[i-1][j]
                if j >= 1 and obstacleGrid[i][j-1] != 1:
                    m_rels[i][j] += m_rels[i][j-1]
        return m_rels[m-1][n-1]


test_rels = [[0]*3 for _ in range(3)]
test_rels[1][1] = 1
c = Solution()
print(c.uniquePathsWithObstacles(test_rels))
