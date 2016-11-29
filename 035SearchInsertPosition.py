class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        
        m_len = len(nums)
        low, high = 0, m_len-1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                while (mid-1) >= 0 and nums[mid-1] == target:
                    mid -= 1
                return mid
        if nums[low] == target:
            while (low-1) >= 0 and nums[low-1] == target:
                    low -= 1
            return low
        elif nums[low] > target:
            return low
        else:
            return low+1
        
c = Solution()
print(c.searchInsert([1,3],2))
print(c.searchInsert([1,3,5,6], 5))
print(c.searchInsert([1,3,5,6], 2))
print(c.searchInsert([1,3,5,6], 7))
print(c.searchInsert([1,3,5,6], 0))
