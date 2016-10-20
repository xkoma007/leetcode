
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        rlist = [0, 1, 2]

        for i in range(3, n+1):
            m_val = rlist[i-1] + rlist[i-2]
            rlist.append(m_val)

        return rlist[n]

c = Solution()
print c.climbStairs(35)
