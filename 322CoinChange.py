class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 1:
            return 0
        m_rel = [0] * (amount+1)

        for i in range(1, amount+1):
            cur_min = -1
            for coin in coins:
                if i >= coin and m_rel[i-coin] != -1:
                    tmp_min = 1 + m_rel[i-coin]
                    if cur_min == -1:
                        cur_min = tmp_min
                    else:
                        cur_min = tmp_min if tmp_min < cur_min else cur_min
            m_rel[i] = cur_min
        return m_rel[amount]

c = Solution()
print(c.coinChange([1, 2, 5], 11))
