class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        m_rels = [0]
        for i in range(1, num+1):
            m_rels.append(m_rels[i >> 1] + (i & 1))
        return m_rels
                
            

c = Solution()
print(c.countBits(4))
