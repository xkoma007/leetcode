class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        find the reginon
        1- 9
        10-99
        100-999
        ....
        100000000-999999999
        """
        for i in range(9):
            d = 9 * 10 ** i
            if n <= d * (i+1):
                break
            else:
                n -= d * (i + 1)
        n -= 1

        return int(str(10**i + n/(i + 1))[n % (i + 1)])
