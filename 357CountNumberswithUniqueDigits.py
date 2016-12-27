class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        total_sum, tmp_val = 0, 9
        for i in range(1, n+1):
            if i == 1:
                total_sum += 10
            elif i > 11:
                break
            else:
                tmp_val *= 11 - i
                total_sum += tmp_val
        return total_sum

c = Solution()
print(c.countNumbersWithUniqueDigits(2))
