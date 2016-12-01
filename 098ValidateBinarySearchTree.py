# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def is_valid_bst(self, root, node, m_rels):
        if node.val in m_rels:
            return False
        else:
            m_rels.append(node.val)
        if not self.search_tree(root, node.val):
            return False
        if node.left:
            if not self.is_valid_bst(root, node.left, m_rels):
                return False
        if node.right:
            if not self.is_valid_bst(root, node.right, m_rels):
                return False
        return True

    def search_tree(self, node, val):
        if not node:
            return False
        if node.val == val:
            return True
        elif node.val > val:
            return self.search_tree(node.left, val)
        else:
            return self.search_tree(node.right, val)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        m_rels = []
        return self.is_valid_bst(root, root, m_rels)
