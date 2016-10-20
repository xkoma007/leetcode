class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m_len = len(s)
        if s == "" or m_len == 1or s.isspace():
            return True
        i = 0
        j = m_len - 1
        bRel = True
        while i < j:
            while (not s[i].isalnum()) and i < j:
                i += 1
            if i == j:
                break
            while (not s[j].isalnum()) and j > i:
                j -= 1
            if j == i:
                break
            if s[i].isalpha() and s[j].isalpha():
                if s[i].lower() != s[j].lower():
                    bRel = False
                    break
            elif s[i].isdigit() and s[j].isdigit():
                if s[i] != s[j]:
                    bRel = False
                    break
            else:
                bRel = False
                break
            j -= 1
            i += 1
        return bRel

c = Solution()
print(c.isPalindrome("A man, a plan, a canal: Panama"))
print(c.isPalindrome("  "))
print(c.isPalindrome(".,"))
print(c.isPalindrome("\"Sue,\" Tom smiles  \"Selim smote us.\""))
