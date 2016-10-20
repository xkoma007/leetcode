# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p is None and q is not None) or (q is None and p is not None):
            return False
        if p is None and q is None:
            return True

        if p.val != q.val:
            return False
        else:
            if self.isSameTree(p.left, q.left) is False:
                return False
            if self.isSameTree(p.right, q.right) is False:
                return False

        return True
