class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_stack = []
        pos = 0
        m_len = len(path)
        rels = ""

        while pos < m_len:
            if path[pos] == '/':
                if (len(path_stack) and path_stack[-1] != '/') or not len(path_stack):
                    path_stack.append('/')
                while pos < m_len and path[pos] == '/':
                    pos += 1
            elif path[pos] == '.':
                if (pos+1) == m_len or path[pos+1] == '/':
                    pos += 1
                elif (path[pos+1] == '.') and ((pos+2) == m_len or path[pos+2] == '/'):
                    if len(path_stack) > 1:
                        path_stack.pop()
                        path_stack.pop()
                    pos += 2
                else:
                    start_pos = pos
                    while pos < m_len:
                        if path[pos] == '/':
                            break
                        pos += 1
                    path_stack.append(path[start_pos:pos])
            else:
                start_pos = pos
                while pos < m_len:
                    if path[pos] == '/' or path[pos] == '.':
                        break
                    else:
                        pos += 1
                path_stack.append(path[start_pos:pos])

        if len(path_stack) > 1 and path_stack[-1] == '/':
            path_stack.pop()

        while len(path_stack):
            rels = path_stack.pop() + rels
        return rels
c = Solution()
print(c.simplifyPath("/..."))
print(c.simplifyPath("/a/./b/../../c/"))
print(c.simplifyPath("/..hidden"))
print(c.simplifyPath("/.ssh/../"))
