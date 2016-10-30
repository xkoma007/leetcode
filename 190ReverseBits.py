class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for pos in range(32):
            res |= ((n >> pos) & 1) << (31 - pos)
        return res

c = Solution()
print(c.reverseBits(43261596))
