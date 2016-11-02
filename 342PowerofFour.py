# -*- coding: utf-8 -*-
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        4  100
        16 10000
        64 1000000
        256 100000000
        观察可知4的次方对应的二进制表示有两个性质:
        1. 首位为１其余位均为０  ->  num  & (num-1) == 0
        2. 后跟偶数个000 -> num & 0x55555555 == num
        """
        return num > 0 and num & (num - 1) == 0 and (num & 0x55555555 == num)
c = Solution()
print(c.isPowerOfFour(256))
