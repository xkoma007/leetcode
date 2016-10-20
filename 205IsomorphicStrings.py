class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m_repls = dict()
        m_vallst = []

        for (x, y) in zip(s, t):
            if x not in m_repls:
                if y not in m_vallst:
                    m_repls[x] = y
                    m_vallst.append(y)
                else:
                    return False
            else:
                if m_repls[x] != y:
                    return False
        return True


c = Solution()
print(c.isIsomorphic("paper", "title"))
