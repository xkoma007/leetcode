class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start_pos, max_len, m_len, map_s = 0, 0, len(s), dict()
        for pos, ch in enumerate(s):
            if ch not in map_s:
                map_s[ch] = pos
            else:
                if start_pos > map_s[ch]:
                    map_s[ch] = pos
                else:
                    max_len = max(pos - start_pos, max_len)
                    start_pos = map_s[ch] + 1
                    map_s[ch] = pos
        max_len = max(m_len - start_pos, max_len)
        return max_len

c = Solution()
print(c.lengthOfLongestSubstring("aab"))
print(c.lengthOfLongestSubstring("bbbbbbb"))
print(c.lengthOfLongestSubstring("pwwkew"))
