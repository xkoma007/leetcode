# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubTreeSymmetric(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        elif left.val != right.val:
            return False
        else:
            if self.isSubTreeSymmetric(left.left, right.right) and self.isSubTreeSymmetric(left.right, right.left):
                return True
            return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        elif self.isSubTreeSymmetric(root.left, root.right) is True:
            return True
        else:
            return False
