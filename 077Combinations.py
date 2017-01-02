class Solution(object):
    def com_kind(self, start, end, cur_rel, kind, total_rels):
        if (end - start + 1) < kind:
            return

        if kind == 1:
            for i in range(start, end+1):
                tmp_rel = cur_rel + [i]
                total_rels.append(tmp_rel)
            return
        for i in range(start, end+1):
            tmp_rel = cur_rel + [i]
            self.com_kind(i+1, end, tmp_rel, kind-1, total_rels)
        return

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n <= 0 or k <= 0 or n < k:
            return []

        total_rels = []
        self.com_kind(1, n, [], k, total_rels)
        return total_rels

c = Solution()
print(c.combine(4, 2))
