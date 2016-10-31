# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def genTreePaths(self, cur_node, cur_path, paths):
        if not cur_node:
            return

        if cur_path:
            cur_path += "->" + str(cur_node.val)
        else:
            cur_path = str(cur_node.val)

        if not cur_node.left and not cur_node.right:
            paths.append(cur_path)
            return
        else:
            if cur_node.left:
                self.genTreePaths(cur_node.left, cur_path, paths)
            if cur_node.right:
                self.genTreePaths(cur_node.right, cur_path, paths)
        return

    def binaryTreePaths(self, root):
        paths, cur_path = [], ""
        self.genTreePaths(root, cur_path, paths)
        return paths
