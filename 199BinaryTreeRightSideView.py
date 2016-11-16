from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class NewTreeNode(object):
    def __init__(self, node, depth):
        self.node = node
        self.depth = depth


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        m_rels = []
        m_queue = deque([])
        new_root = NewTreeNode(root, 0)
        m_queue.append(new_root)
        cur_depth, right_val = 0, 0
        while len(m_queue):
            if m_queue[0].depth > cur_depth:
                cur_depth += 1
                m_rels.append(right_val)
            else:
                cur_node = m_queue.popleft()
                right_val = cur_node.node.val
                if cur_node.node.left:
                    new_node = NewTreeNode(cur_node.node.left, cur_depth+1)
                    m_queue.append(new_node)
                if cur_node.node.right:
                    new_node = NewTreeNode(cur_node.node.right, cur_depth+1)
                    m_queue.append(new_node)
        m_rels.append(right_val)
        return m_rels
