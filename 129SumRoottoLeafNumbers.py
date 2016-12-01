# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sum_paths(self, node, cur_paths):
        if not node.left and not node.right:
            cur_paths += str(node.val)
            return int(cur_paths)
        total_sum = 0
        if node.left:
            total_sum += self.sum_paths(node.left, cur_paths + str(node.val))
        if node.right:
            total_sum += self.sum_paths(node.right, cur_paths + str(node.val))
        return total_sum

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.sum_paths(root, "")

c = Solution()
import test_utils
root = test_utils.gen_tree_by_list([1, 2, 3])
print(c.sumNumbers(root))
