from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def gen_tree_by_list(items):
    if not items:
        return None
    m_queue = deque([])
    root = TreeNode(items[0])
    pos = 1
    m_len = len(items)
    m_queue.append(root)
    while pos <= (m_len - 1):
        if not len(m_queue):
            break
        cur_node = m_queue.popleft()
        if items[pos]:
            left_node = TreeNode(items[pos])
            cur_node.left = left_node
            m_queue.append(left_node)
        if (pos+1) <= (m_len-1):
            if items[pos+1]:
                right_node = TreeNode(items[pos+1])
                cur_node.right = right_node
                m_queue.append(right_node)
        pos += 2
    return root
