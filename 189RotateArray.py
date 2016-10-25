class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        m_len = len(nums)
        if not m_len:
            return
        k = k % m_len
        for i in range(k):
            nums.insert(0, nums.pop())
        return nums

c = Solution()
print(c.rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(c.rotate([1, 2, 3, 4, 5, 6, 7], 7))
