class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_len = 1
        m_lens = []
        for i, cur_val in enumerate(nums):
            m_lens.append(1)
            for j in range(i):
                if cur_val > nums[j]:
                    if m_lens[j] + 1 > m_lens[i]:
                        m_lens[i] = m_lens[j] + 1 if (m_lens[j] + 1) > m_lens[j] else m_lens[i]
                        max_len = m_lens[i] if m_lens[i] > max_len else max_len
        return max_len

c = Solution()
print(c.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(c.lengthOfLIS([2, 2]))
