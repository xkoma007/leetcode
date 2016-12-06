class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        all_max = nums[0]
        for pos, val in enumerate(nums):
            if pos == 0:
                m_rels = [[nums[0], nums[0]]]
                continue
            cur_rel = [nums[pos] * m_rels[pos-1][0], nums[pos] * m_rels[pos-1][1], nums[pos]]
            cur_rel.sort()
            print(cur_rel)
            m_rels.append([cur_rel[2], cur_rel[0]])
            all_max = cur_rel[2] if cur_rel[2] > all_max else all_max

        return all_max

c = Solution()
print(c.maxProduct([2,3,-2,4]))
