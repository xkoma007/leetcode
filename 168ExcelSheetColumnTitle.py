class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
             "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
             "W", "X", "Y", "Z")
        k = n
        str = ""
        while k > 0:
            str += i[k % 26-1]
            if k % 26 == 0:
                k = k / 26 - 1
            else:
                k /= 26
        return str[::-1]


a = Solution()
print a.convertToTitle(52)
