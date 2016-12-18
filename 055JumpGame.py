class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for i, cur_val in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + cur_val)
        return True
