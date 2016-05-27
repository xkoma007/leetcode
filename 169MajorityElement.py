class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m_len = len(nums)
        m_sets = dict()
        m_max = 0
        for i, val in enumerate(nums):
            if val in m_sets:
                m_count = m_sets.get(val)
                m_count += 1
                m_sets[val] = m_count
            else:
                m_sets[val] = 1

        for key in m_sets:
            if m_sets[key] > m_len / 2:
                m_max = key
                break
        
        return m_max
