class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_hash = dict()
        for m_pos, m_val in enumerate(nums):
            if m_val not in nums_hash:
                nums_hash[m_val] = m_pos
            else:
                if (m_pos - nums_hash[m_val]) <= k:
                    return True
                else:
                    nums_hash[m_val] = m_pos
        return False
