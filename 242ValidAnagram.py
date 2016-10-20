class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "" and t == "":
            return True
        if len(s) != len(t):
            return False

        m_hash = dict()
        for key in s:
            if key in m_hash:
                m_hash[key] += 1
            else:
                m_hash[key] = 1

        for key in t:
            if key in m_hash:
                if m_hash[key] == 1:
                    del m_hash[key]
                else:
                    m_hash[key] -= 1
            else:
                break

        if len(m_hash) != 0:
            return False

        return True


c = Solution()
print(c.isAnagram("anagram", "nagaram"))
print(c.isAnagram("rat", "car"))
