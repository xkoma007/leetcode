class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        m_stack = []
        for val in tokens:
            if val == '+':
                fval = m_stack.pop()
                sval = m_stack.pop()
                new_val = sval + fval
                m_stack.append(new_val)
            elif val == '-':
                fval = m_stack.pop()
                sval = m_stack.pop()
                new_val = sval - fval
                m_stack.append(new_val)
            elif val == '*':
                fval = m_stack.pop()
                sval = m_stack.pop()
                new_val = sval * fval
                m_stack.append(new_val)
            elif val == '/':
                fval = m_stack.pop()
                sval = m_stack.pop()
                new_val = sval / fval
                if new_val < 0:
                    new_val = -sval/fval
                    new_val = -new_val
                m_stack.append(new_val)
            else:
                m_stack.append(int(val))
        return m_stack.pop()
c = Solution()
# print(c.evalRPN(["2", "1", "+", "3", "*"]))
# print(c.evalRPN(["4", "13", "5", "/", "+"]))
print(c.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
