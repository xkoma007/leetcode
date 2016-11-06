class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map_s1, rels = dict(), []
        for ch in nums1:
            if ch not in map_s1:
                map_s1[ch] = 1
            else:
                map_s1[ch] += 1

        for ch in nums2:
            if ch in map_s1 and map_s1[ch] > 0:
                map_s1[ch] -= 1
                rels.append(ch)
        return rels

c = Solution()
print(c.intersect([1, 2, 2, 1], [2, 2]))
