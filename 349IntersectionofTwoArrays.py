class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        map_table = dict()
        rels = []
        for val in nums1:
            if val not in map_table:
                map_table[val] = 0
        for val in nums2:
            if val in map_table and map_table[val] == 0:
                map_table[val] = 1
                rels.append(val)
        return rels
c = Solution()
print(c.intersection([1, 2, 2, 1], [2, 2]))
