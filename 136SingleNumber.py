class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        m_rel = nums[0] ^ nums[1]
        for m_val in nums[2:]:
            m_rel = m_rel ^ m_val
        return m_rel

c = Solution()
print(c.singleNumber([1,2,2,1,6]))
