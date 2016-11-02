class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        new_rels = list(s)
        vowel_rels = []
        for pos, ch in enumerate(new_rels):
            if ch.lower() in vowels:
                vowel_rels.append(pos)
        m_len = len(vowel_rels)
        if m_len == 0 or m_len == 1:
            return s
        else:
            max_pos = m_len - 1
            for pos in range(m_len//2):
                 new_rels[vowel_rels[pos]], new_rels[vowel_rels[max_pos-pos]] = new_rels[vowel_rels[max_pos-pos]], new_rels[vowel_rels[pos]]
            return ''.join(new_rels)
c = Solution()
print(c.reverseVowels("hello"))
print(c.reverseVowels("leetcode"))
print(c.reverseVowels("aA"))
