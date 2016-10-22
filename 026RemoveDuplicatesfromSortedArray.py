class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        m_len = len(nums)
        i = 1
        for j in range(m_len):
            if nums[j] != nums[i-1]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return len(nums[:i])

c = Solution()
print(c.removeDuplicates([1, 1, 2, 8, 8, 9, 20, 21, 21]))
