class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m_len = len(nums)
        low, high = 0, m_len - 1
        start, end = -1, -1
        if not nums:
            return [start, end]
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                start, end = mid, mid
                while start > 0 and nums[start] == nums[start-1]:
                    start -= 1
                while end < (m_len-1) and nums[end] == nums[end+1]:
                    end += 1
                break
        return [start, end]

c = Solution()
print(c.searchRange([5, 7, 7, 8, 8, 10], 8))
print(c.searchRange([1], 1))
