# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def depth_paths(self, node, cur_sum,  cur_paths, sum_paths):
        if not node.left and not node.right:
            cur_paths.append(node.val)
            if cur_sum == sum(cur_paths):
                sum_paths.append(cur_paths)
            return

        if node.left:
            left_paths = cur_paths + [node.val]
            self.depth_paths(node.left, cur_sum, left_paths, sum_paths)
        if node.right:
            right_paths = cur_paths + [node.val]
            self.depth_paths(node.right, cur_sum, right_paths, sum_paths)
        return

    def pathSum(self, root, cur_sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        cur_paths, sum_paths = [], []
        self.depth_paths(root, cur_sum, cur_paths, sum_paths)
        return sum_paths

c = Solution()
import test_utils
null=None
root=test_utils.gen_tree_by_list([5,4,8,11,null,13,4,7,2,null,null,5,1])
print(c.pathSum(root, 22))
