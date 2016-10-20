class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num <= 0:
            return False
        
        prime_factors = [2,3,5]
        for m_val in prime_factors:
            while num % m_val == 0:
                num = num // m_val
        if num == 1:
            return True
        else:
            return False
        
c = Solution()
print(c.isUgly(937351770))
