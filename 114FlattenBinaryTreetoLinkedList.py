# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pre_travel_tree(self, node, rels):
        if not node:
            return
        rels.append(node)
        self.pre_travel_tree(node.left, rels)
        self.pre_travel_tree(node.right, rels)

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        rels = []
        self .pre_travel_tree(root, rels)
        last_node = None
        for cur_node in rels[::-1]:
            cur_node.left = None
            cur_node.right = last_node
            last_node = cur_node
        test(root)
        return


def test(root):
    while root:
        print(root.val)
        root = root.right

import test_utils
root = test_utils.gen_tree_by_list([1, 2])
c = Solution()
print(c.flatten(root))
