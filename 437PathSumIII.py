# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def top_node(self, node, sum):
        res = 0
        if not node:
            return 0
        if node.val == sum:
            res += 1
        return res + self.top_node(node.left, sum-node.val) + self.top_node(node.right, sum-node.val)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.top_node(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
