class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        m_len = len(nums)
        pos = 0
        for _ in range(m_len):
            if nums[pos] == 0:
                nums.remove(0)
                nums.append(0)
            else:
                pos += 1
        return
