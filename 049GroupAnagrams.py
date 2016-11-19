class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        all_maps = []
        m_rels = []
        for cur_str in strs:
            match = False
            cur_map = dict()
            for ch in cur_str:
                if ch not in cur_map:
                    cur_map[ch] = 1
                else:
                    cur_map[ch] += 1
            for pos, tmp_map in enumerate(all_maps):
                if cmp(cur_map, tmp_map) == 0:
                    m_rels[pos].insert(0, cur_str)
                    match = True
                    break
            if not match:
                all_maps.append(cur_map)
                m_rels.append([cur_str])
        return m_rels
c = Solution()
print(c.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
