class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        rel = [0] * (n+1)
        rel[0] = 1
        print(rel)
        for i in range(1, n+1):
            for j in range(1, i+1):
                rel[i] += rel[j-1] * rel[i-j]
        return rel[n]

c = Solution()
print(c.numTrees(3))
