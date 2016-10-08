class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.m_stack = []
        self.b_empty = True
        self.m_minlst = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.m_stack.append(x)
        if self.b_empty:
            self.b_empty = False
            self.m_minlst.append(x)
        else:
            if x <= self.m_minlst[-1]:
                self.m_minlst.append(x)
        return

    def pop(self):
        """
        :rtype: void
        """
        if not self.b_empty:
            m_curval = self.m_stack.pop()
            if not self.m_stack:
                self.m_minlst.pop()
                self.b_empty = True
            else:
                if m_curval == self.m_minlst[-1]:
                    self.m_minlst.pop()
        return

    def top(self):
        """
        :rtype: int
        """
        if not self.b_empty:
            return self.m_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.b_empty:
            return self.m_minlst[-1]

# Your MinStack object will be instantiated and called as such:

# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
