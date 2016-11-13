import test_utils
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        m_queue = deque([])
        m_rels, tmp_rel = [], []
        new_root = NewTreeNode(root, 0)
        m_queue.append(new_root)
        cur_depth = 0
        reverse = False
        while len(m_queue):
            if m_queue[0].depth > cur_depth:
                cur_depth += 1
                if not reverse:
                    reverse = True
                else:
                    tmp_rel.reverse()
                    reverse = False
                m_rels.append(tmp_rel)
                tmp_rel = []
            else:
                cur_node = m_queue.popleft()
                if cur_node.node.left:
                    new_node = NewTreeNode(cur_node.node.left, cur_depth+1)
                    m_queue.append(new_node)
                if cur_node.node.right:
                    new_node = NewTreeNode(cur_node.node.right, cur_depth+1)
                    m_queue.append(new_node)
                tmp_rel.append(cur_node.node.val)
        if reverse:
            tmp_rel.reverse()
        m_rels.append(tmp_rel)
        return m_rels

null = None
def test():
    root = test_utils.gen_tree_by_list([1,2,3,4,null,null,5])
    c = Solution()
    print(c.zigzagLevelOrder(root))

test()
