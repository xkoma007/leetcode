class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        # sliding windows
        """
        rels = []
        map_p, map_s = dict(), dict()
        p_len, s_len = len(p), len(s)
        for ch in p:
            if ch not in map_p:
                map_p[ch] = 1
            else:
                map_p[ch] = map_p[ch] + 1

        if s_len < p_len:
            return rels
        count = 0
        while count < s_len:
            if s[count] not in map_s:
                map_s[s[count]] = 1
            else:
                map_s[s[count]] += 1

            if count >= p_len:
                map_s[s[count-p_len]] -= 1
            if count >= p_len - 1:
                # compare
                success = True
                for k in map_p.keys():
                    if k not in map_s or map_p[k] != map_s[k]:
                        success = False
                if success:
                    rels.append(count-p_len+1)
            count += 1
        return rels
c = Solution()
# print(c.findAnagrams("abab", "ab"))
print(c.findAnagrams("cbaebabacd", "abc"))
