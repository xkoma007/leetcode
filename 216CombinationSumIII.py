class Solution(object):
    def combination_sum(self, start, k, num_sum, cur_rel, total_rels):
        if k == 0 and num_sum == 0:
            total_rels.append(cur_rel)
            return
        if (k == 0 and num_sum > 0) or (k > 0 and num_sum == 0):
            return

        min_num = num_sum if num_sum < 9 else 9
        for i in range(start, min_num+1):
            if i not in cur_rel:
                new_rel = cur_rel + [i]
                self.combination_sum(i+1, k-1, num_sum-i, new_rel, total_rels)
        return

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        m_rels = []
        min_num = n if n < 9 else 9
        for i in range(1, min_num+1):
            cur_rel = [i]
            self.combination_sum(i+1, k-1, n-i, cur_rel, m_rels)
        return m_rels

c = Solution()
print(c.combinationSum3(3, 9))
