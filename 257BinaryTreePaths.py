# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def genTreePaths(self, node, path):
        pass

    def binaryTreePaths(self, root):
        m_paths = [] 
        if root is None:
            return m_paths

        path = root.val
        
        sleft = self.genTreePaths(root.left, path)
        sright = self.genTreePaths(root.right, path)

        m_paths
        return path
        
