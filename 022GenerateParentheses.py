class Solution(object):
    def gen_parentheses(self, left_num,right_num, cur_parent, m_rels):
        if left_num == 0 and left_num == right_num:
            m_rels.append(cur_parent)
        if left_num == right_num:
            self.gen_parentheses(left_num-1, right_num, cur_parent+"(", m_rels)
        else:
            if left_num >= 1:
                self.gen_parentheses(left_num-1, right_num, cur_parent+"(", m_rels)
            if right_num >= 1:
                self.gen_parentheses(left_num, right_num-1, cur_parent+")", m_rels)
        return
        
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        m_rels = []
        self.gen_parentheses(n, n, "", m_rels)
        return m_rels
    
c = Solution()
print(c.generateParenthesis(3))
