class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num // 10 == 0:
            return num

        count = 0
        while num != 0:
            count += num % 10
            num = num // 10

        return self.addDigits(count)


a = Solution()
print(a.addDigits(138))
