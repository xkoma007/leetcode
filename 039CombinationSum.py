class Solution(object):
    def com_sum(self, left_nums, target, cur_rel, rels):
        if target == 0 and cur_rel:
            cur_rel.sort()
            if cur_rel not in rels:
                rels.append(cur_rel)
            return
        if target > 0 and not left_nums:
            return
        for pos, val in enumerate(left_nums):
            if val <= target:
                new_rel = cur_rel + [val]
                self.com_sum(left_nums[pos:], target-val, new_rel, rels)
        return

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        m_rels = []
        self.com_sum(candidates, target, [], m_rels)
        return m_rels

c = Solution()
print(c.combinationSum([10,1,2,7,6,1,5], 8))
