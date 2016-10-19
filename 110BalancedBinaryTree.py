# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def subTreesDepth(self, node):
        m_height = 0
        if node is None:
            return m_height
        else:
            m_height = 1
            m_lheight = self.subTreesDepth(node.left)
            m_rheight = self.subTreesDepth(node.right)
            if m_lheight > m_rheight:
                m_height += m_lheight
            else:
                m_height += m_rheight
        return m_height

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if abs(self.subTreesDepth(root.left) - self.subTreesDepth(root.right)) > 1:
            return False
        else:
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False
