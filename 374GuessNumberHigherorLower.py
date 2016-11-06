# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    if num < 6:
        return 1
    elif num > 6:
        return -1
    else:
        return 0


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while True:
            guess_val = (low + high) // 2
            g = guess(guess_val)
            if g == 0:
                return guess_val
            elif g == 1:
                low = guess_val + 1
            else:
                high = guess_val - 1

c = Solution()
print(c.guessNumber(10))
