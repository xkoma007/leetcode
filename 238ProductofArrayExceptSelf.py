class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m_rels = [1]
        m_len = len(nums)
        for pos in range(1, m_len):
            m_rels.append(nums[pos-1] * m_rels[pos-1])
        num = 1
        for pos in range(m_len-1, -1, -1):
            m_rels[pos] *= num
            num *= nums[pos]
        return m_rels

c = Solution()
print(c.productExceptSelf([1, 2, 3, 4]))
print(c.productExceptSelf([0, 0]))
