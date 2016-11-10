class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        primes_list = [True] * n

        i = 2
        while (i ** 2) < n:
            if primes_list[i]:
                j = i ** 2
                while j < n:
                    primes_list[j] = False
                    j += i
            i += 1

        count = 0
        for pos in range(2, n):
            if primes_list[pos]:
                count += 1
        return count

c = Solution()
print(c.countPrimes(1500000))
