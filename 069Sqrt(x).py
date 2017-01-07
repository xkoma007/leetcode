class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        guess = 1.0
        while abs(x - guess * guess) > 0.001:
            guess = (guess + x/guess) / 2
        return int(guess)

c = Solution()
print(c.mySqrt(1))
