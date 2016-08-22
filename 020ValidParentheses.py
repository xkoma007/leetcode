class Solution(object):
    def cmp_oper(self, leftoper, right):
        success = False

        if leftoper == '(' and right == ')':
            success = True
        elif leftoper == '[' and right == ']':
            success = True
        elif leftoper == '{' and right == '}':
            success = True
        return success

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m_list = []
        m_len = len(s)
        k = 0
        m_leftoper = ['(', '{', '[']
        m_rightoper = [')', '}', ']']
        m_success = True

        while k < m_len:
            if s[k] in m_leftoper:
                m_list.append(s[k])
            elif s[k] in m_rightoper:
                if not m_list:
                    m_success = False
                    break
                elif not self.cmp_oper(m_list.pop(), s[k]):
                    m_success = False
                    break
            else:
                k += 1

        if m_list:
            m_success = False
        return m_success
