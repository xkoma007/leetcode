# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def is_ancestor_node(self, parent, cur_node):
        if not parent:
            return False
        elif parent is cur_node:
            return True
        else:
            if self.is_ancestor_node(parent.left, cur_node):
                return True
            elif self.is_ancestor_node(parent.right, cur_node):
                return True
            else:
                return False

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if self.is_ancestor_node(root, p) and self.is_ancestor_node(root, q):
            m_left = self.lowestCommonAncestor(root.left, p, q)
            if m_left:
                return m_left
            m_right = self.lowestCommonAncestor(root.right, p, q)
            if m_right:
                return m_right
            return root
        else:
            return None
