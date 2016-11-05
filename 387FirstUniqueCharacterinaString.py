class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        m_rel = -1
        map_s = dict()

        for ch in s:
            if ch not in map_s:
                map_s[ch] = 1
            else:
                map_s[ch] += 1

        for pos in range(len(s)):
            if map_s[s[pos]] == 1:
                m_rel = pos
                break

        return m_rel


f = Solution()
print(f.firstUniqChar('loveleetcode'))
