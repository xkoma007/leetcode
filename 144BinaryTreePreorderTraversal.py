# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        m_stack = []
        m_list = []

        if root:
            m_stack.append(root)
        while len(m_stack):
            new_node = m_stack.pop()
            if new_node.val != '#':
                m_list.append(new_node.val)
            else:
                continue
            if new_node.right:
                m_stack.append(new_node.right)
            if new_node.left:
                m_stack.append(new_node.left)

        return m_list

a = Solution()
print a.preorderTraversal(None)
