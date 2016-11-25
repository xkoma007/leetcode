class Solution(object):
    def gen_strs_by_digits(self, digits, cur_rel, map_s, m_rels):
        if len(digits) == 1:
            for ch in map_s[digits]:
                new_rel = cur_rel + ch
                m_rels.append(new_rel)
        else:
            for ch in map_s[digits[0]]:
                new_rel = cur_rel + ch
                self.gen_strs_by_digits(digits[1:], new_rel, map_s, m_rels)
        return 
                

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map_s = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs",
                 "8":"tuv", "9":"wxyz"}
        if not len(digits):
            return []
        
        m_rels = []
        self.gen_strs_by_digits(digits, "", map_s, m_rels)
        return m_rels
    
c = Solution()
print(c.letterCombinations("23"))
        
