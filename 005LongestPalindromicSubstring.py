class Solution(object):
    def isPalinndrome(self, s, rs, re):
        while rs < re:
            if s[rs] != s[re]:
                return False
            rs += 1
            re -= 1
        return True
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        m_len, cur_max = len(s), 0
        rs, re = 0, 0
        for pos in range(m_len):
            if self.isPalinndrome(s, pos-cur_max, pos):
                rs, re = pos-cur_max, pos
                cur_max += 1
            elif (pos-cur_max-1) >= 0 and self.isPalinndrome(s, pos-cur_max-1, pos):
                rs, re = pos-cur_max-1, pos
                cur_max += 2
        return s[rs:re+1]

c = Solution()
print(c.longestPalindrome("cbbd"))
 
