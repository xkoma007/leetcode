class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        m_len = len(nums)
        m_rels = []
        for i in range(m_len-2):
            if (i == 0 or (i > 0 and nums[i] != nums[i-1])):
                low = i + 1
                high = m_len - 1
                sum = -nums[i]
                while low < high:
                    if (nums[low] + nums[high]) == sum:
                        m_rels.append([nums[i], nums[low], nums[high]])
                        while low < high and nums[high] == nums[high-1]:
                            high -= 1
                        while low < high and nums[low] == nums[low+1]:
                            low += 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < sum:
                        low += 1
                    else:
                        high -= 1
        return m_rels
c = Solution()
print(c.threeSum([-1, 0, 1, 2, -1, -4]))
