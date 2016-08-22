class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        m_len = len(needle)
        m_pos = -1
        
        if haystack == needle:
            return 0
        if m_len == 0:
            return 0

        for i,ch in enumerate(haystack):
            if needle[0] == ch:
                j, k = i, i
            else:
                continue
 
            if len(haystack) - j < m_len:
                continue


            for ch in needle:
                if ch != haystack[k]:
                    break
                k += 1
            if k - j == m_len:
                m_pos = j
                break

        return m_pos
                
a = Solution()
print a.strStr("aaa","a")
            
