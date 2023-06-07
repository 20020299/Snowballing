class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def insert(temp, data):
    que = []
    que.append(temp)
    while len(que):
        temp = que[0]
        que.pop(0)
        if not temp.left:
            temp.left = TreeNode(data)
            break
        else:
            que.append(temp.left)
        if not temp.right:
            temp.right = TreeNode(data)
            break
        else:
            que.append(temp.right)


def make_tree(elements):
    Tree = TreeNode(elements[0])
    for element in elements[1:]:
        insert(Tree, element)
    return Tree


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
      :type root: TreeNode
      :rtype: int
      """
        self.ans = 0
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.ans = max(self.ans, right + left)
        return max(left + 1, right + 1)


root = make_tree([1, 2, 3, 4, 5])
ob1 = Solution()
print(ob1.diameterOfBinaryTree(root))
