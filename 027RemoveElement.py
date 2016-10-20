class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        while val in nums:
            nums.remove(val)

        return len(nums)

a = Solution()
print a.removeElement([3, 2, 2, 3], 3)
