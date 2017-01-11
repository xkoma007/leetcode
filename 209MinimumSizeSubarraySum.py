class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        m_len = len(nums)
        m_min = 0
        i, j = 0, 0
        cur_sum = 0
        while j < m_len:
            cur_sum += nums[j]
            j += 1
            while cur_sum >= s:
                m_min = (j-i) if m_min == 0 else min(j-i, m_min)
                cur_sum -= nums[i]
                i += 1
        return m_min
