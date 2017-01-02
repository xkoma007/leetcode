class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m_len = len(nums)
        total_len = m_len
        repeat_num, repeat_val = 0, 0

        for i in range(m_len-1, -1, -1):
            if repeat_num == 0 or nums[i] != repeat_val:
                repeat_val = nums[i]
                repeat_num = 1
            elif nums[i] == repeat_val:
                repeat_num += 1
                if repeat_num > 2:
                    total_len -= 1
                    del nums[i]

        return total_len

c = Solution()
print(c.removeDuplicates([1,1,1,2,2,3]))
