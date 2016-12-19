# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob_sub(self, root):
        if not root:
            return [0, 0]

        left = self.rob_sub(root.left)
        right = self.rob_sub(root.right)
        print(left, right)
        res_left = max(left[0], left[1]) + max(right[0], right[1])
        res_right = root.val + left[0] + right[0]
        return [res_left, res_right]

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        m_rel = self.rob_sub(root)
        return m_rel[0] if m_rel[0] > m_rel[1] else m_rel[1]

import test_utils
null = None
root = test_utils.gen_tree_by_list([3,2,3,null,3,null,1])
c = Solution()
print(c.rob(root))
