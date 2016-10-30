class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            count += n % 2
            n = n / 2
        return count

c = Solution()
print(c.hammingWeight(11))
