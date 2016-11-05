class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        # binary search
        """
        if n <= 0:
            return 0
        low, high, guess_line = 1, n, n
        while True:
            guess_line = (low + high) // 2
            guess_val = ((guess_line + 1) * guess_line) // 2
            if n > guess_val:
                if n < (guess_val + guess_line + 1):
                    break
                else:
                    low = guess_line + 1
            elif n < guess_val:
                high = guess_line - 1
            else:
                break
        return guess_line
c = Solution()
print(c.arrangeCoins(8))
