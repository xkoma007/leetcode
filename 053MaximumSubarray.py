class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m_sum = 0
        m_rels = []
        for i, val in enumerate(nums):
            if i == 0:
                m_rels.append(val)
                m_sum = val
                continue
            if m_rels[i-1] < 0:
                m_rels.append(val)
            else:
                m_rels.append(m_rels[i-1]+val)
            m_sum = max(m_sum, m_rels[i])
        return m_sum
