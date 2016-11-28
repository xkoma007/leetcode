class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        m_len = len(nums)
        a, b = [0], []

        if m_len == 1:
            return nums[0]
        for i in range(m_len):
            if i > 0:
                if i == 1:
                    a.append(nums[i])
                elif i == 2:
                    cur_max = max(nums[i-1], nums[i])
                    a.append(cur_max)
                else:
                    cur_max = max(a[i-2] + nums[i], a[i-1])
                    a.append(cur_max)
            if i < (m_len - 1):
                if i == 0:
                    b.append(nums[i])
                elif i == 1:
                    cur_max = max(nums[i], nums[i-1])
                    b.append(cur_max)
                else:
                    cur_max = max(b[i-2] + nums[i], b[i-1])
                    b.append(cur_max)
        max_rel = max(a[-1], b[-1])
        return max_rel
c = Solution()
print(c.rob([1, 7, 9,2]))
