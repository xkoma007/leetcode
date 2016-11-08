from collections import deque
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = deque([])

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q.append(x)
        for _ in range(len(self.q)-1):
            x = self.q.popleft()
            self.q.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.empty():
            return self.q.popleft()

    def top(self):
        """
        :rtype: int
        """
        
        if not self.empty():
            return self.q[0]
        
    def empty(self):
        """
        :rtype: bool
        """
        if not len(self.q):
            return True
        else:
            return False
