class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m_len = len(nums)
        if m_len == 0:
            return 0
        if m_len == 1:
            return nums[0]
        f = []
        f.append(nums[0])
        max = nums[1] if nums[1] > nums[0] else nums[0]
        f.append(max)
        for pos in range(2, m_len):
            if (nums[pos] + f[pos-2]) >= f[pos-1]:
                max = nums[pos] + f[pos-2]
            else:
                max = f[pos-1]
            f.append(max)

        return f[m_len-1]

c = Solution()
print(c.rob([2, 1, 1, 2]))
