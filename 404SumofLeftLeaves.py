# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def left_sum_node(self, node):
        sum = 0
        if not node:
            return sum
        if node.left:
            if not node.left.left and not node.left.right:
                sum += node.left.val
        return sum + self.left_sum_node(node.left) + self.left_sum_node(node.right)

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.left_sum_node(root)
