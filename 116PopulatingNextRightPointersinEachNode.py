from collections import deque


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        cur_layer = 1
        m_queue = deque([])
        m_queue.append(root)
        while cur_layer != 0:
            next_layer = 0
            while cur_layer > 0:
                node = m_queue.popleft()
                if cur_layer == 1:
                    node.next = None
                else:
                    node.next = m_queue[0]
                if node.left:
                    next_layer += 1
                    m_queue.append(node.left)
                if node.right:
                    next_layer += 1
                    m_queue.append(node.right)
                cur_layer -= 1
            cur_layer = next_layer
        return

c = Solution()
import test_utils
root = test_utils.gen_tree_by_list([1, 2, 3, 4, 5, 6, 7])
print(c.connect(root))

# root  = root.left
# root = root.left

while root:
    print(root.val)
    root = root.next
