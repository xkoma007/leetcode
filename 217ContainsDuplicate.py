class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if not nums:
            return False
        else:
            m_records = dict()
            for m_pos,m_val in enumerate(nums):
                if m_val not in m_records:
                    m_records[m_val] = m_pos
                else:
                    return True
            return False
                    
