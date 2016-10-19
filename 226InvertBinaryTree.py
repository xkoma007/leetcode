# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or (not root.left and not root.right):
            return root
        m_treeleft = root.left
        root.left = root.right
        root.right = m_treeleft
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
