# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        m_remainPath = sum - root.val
        if root.left is None and root.right is None:
            if m_remainPath == 0:
                return True
            else:
                return False

        if self.hasPathSum(root.left, m_remainPath) or self.hasPathSum(root.right, m_remainPath):
            return True
        else:
            return False
