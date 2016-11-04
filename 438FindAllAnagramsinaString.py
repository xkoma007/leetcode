class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        map_p = dict()
        p_len = len(p)
        s_len = len(s)
        for ch in p:
            if ch not in map_p:
                map_p[ch] = 1
            else:
                map_p[ch] = map_p[ch] + 1
        rels = []
        map_s = dict()
        for i in range(s_len):
            compare = True
            map_s.clear()
            if i + p_len <= s_len:
                for j in range(i, i+p_len):
                    if s[j] not in map_p:
                        compare = False
                        break
                    else:
                        if s[j] not in map_s:
                            map_s[s[j]] = 1
                        else:
                            map_s[s[j]] = map_s[s[j]] + 1
                if compare:
                    success = True
                    for ch in map_s:
                        if map_s[ch] != map_p[ch]:
                            success = False
                            break
                    if success:
                        rels.append(i)
        return rels
c = Solution()
# print(c.findAnagrams("abab", "ab"))
print(c.findAnagrams("cbaebabacd", "abc"))
