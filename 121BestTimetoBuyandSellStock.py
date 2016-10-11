class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m_maxProfit = 0

        for i, m_curSell in enumerate(prices):
            if i == 0:
                continue
            elif i == 1:
                m_curMax = prices[i] - prices[i-1]
                if m_curMax > m_maxProfit:
                    m_maxProfit = m_curMax
            else:
                m_minus = prices[i] - prices[i-1]
                m_curMax = m_curMax + m_minus
                if m_minus > m_curMax:
                    m_curMax = m_minus
                if m_curMax > m_maxProfit:
                    m_maxProfit = m_curMax
        return m_maxProfit

c = Solution()
print(c.maxProfit([7, 1, 5, 3, 6, 4]))
print(c.maxProfit([7, 6, 4, 3, 1]))
