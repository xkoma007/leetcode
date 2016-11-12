# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        m_stack, m_rels = [],  []
        cur_node = root
        while True:
            while cur_node:
                m_stack.append(cur_node)
                cur_node = cur_node.left
            if not len(m_stack):
                break
            visited_node = m_stack.pop()
            m_rels.append(visited_node.val)
            cur_node = visited_node.right
        return m_rels
