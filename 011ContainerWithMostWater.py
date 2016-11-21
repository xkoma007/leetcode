class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m_len = len(height)
        i, j = 0, m_len-1
        max_area = 0
        while i < j:
            min_height = min(height[i], height[j])
            max_area = max((j - i) * min_height, max_area)
            while (i < j) and height[i] <= min_height:
                i += 1
            while (i < j) and height[j] <= min_height:
                j -= 1
        return max_area
c = Solution()
print(c.maxArea([1, 1]))
