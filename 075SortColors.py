class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_red, num_white, num_blue = 0, 0, 0

        for val in nums:
            if val == 0:
                num_red += 1
            elif val == 1:
                num_white += 1
            else:
                num_blue += 1

        for pos, val in enumerate(nums):
            if num_red != 0:
                nums[pos] = 0
                num_red -= 1
            elif num_white != 0:
                nums[pos] = 1
                num_white -= 1
            else:
                nums[pos] = 2
                num_blue -= 1
        return
