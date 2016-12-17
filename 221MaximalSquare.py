class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        max_sq = 0
        row, col = len(matrix), len(matrix[0])
        m_rels = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if int(matrix[i][j]) == 0:
                    m_rels[i][j] = 0
                elif i == 0 or j == 0:
                    if int(matrix[i][j]) == 1:
                        max_sq = 1 if max_sq < 1 else max_sq
                        m_rels[i][j] = 1
                else:
                    min_step = min(m_rels[i-1][j], m_rels[i][j-1])
                    min_step = min(m_rels[i-1][j-1], min_step)
                    m_rels[i][j] = min_step + int(matrix[i][j])
                    max_sq = m_rels[i][j] if m_rels[i][j] > max_sq else max_sq
        return max_sq*max_sq
c = Solution()
print(c.maximalSquare(["10100","10111","11111","10010"]))
print(c.maximalSquare(["11", "11"]))
