class Solution(object):
    def sub_sets(self, cur_rel, left_rel, total_rels):
        if not left_rel:
            total_rels.append(cur_rel)
            return
        self.sub_sets(cur_rel, [], total_rels)
        for pos, val in enumerate(left_rel):
            tmp_val = cur_rel + [val]
            self.sub_sets(tmp_val, left_rel[pos+1:], total_rels)
        return

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        m_rels = []
        m_rels.append([])

        for pos, val in enumerate(nums):
            tmp_val = [val]
            self.sub_sets(tmp_val, nums[pos+1:], m_rels)

        return m_rels
c = Solution()
print(c.subsets([1,2,3]))
