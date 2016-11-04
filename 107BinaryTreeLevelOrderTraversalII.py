# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        m_sumValList = []
        m_curTreeList = []
        m_curValList = []

        def curLevelTree(curTreeList):
            m_nextTreeList = []
            from collections import deque
            curTreeQueue = deque(curTreeList)
            while len(curTreeQueue) > 0:
                m_TreeNode = curTreeQueue.popleft()
                if m_TreeNode.left:
                    m_nextTreeList.append(m_TreeNode.left)
                if m_TreeNode.right:
                    m_nextTreeList.append(m_TreeNode.right)
            return m_nextTreeList

        if root:
            m_curTreeList.append(root)
        while m_curTreeList:
            for m_TreeNode in m_curTreeList:
                m_curValList.append(m_TreeNode.val)
            m_sumValList.insert(0, m_curValList)
            m_curValList = []
            m_curTreeList = curLevelTree(m_curTreeList)
        return m_sumValList


def test():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = None
    root.right.left = None
    root.right.right = TreeNode(5)
    c = Solution()
    print(c.levelOrderBottom(root))
test()
