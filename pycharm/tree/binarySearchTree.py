class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        pass

    def insert(self, root, val):
        if root is None:
            return Node(val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        else:
            root.left = self.insert(root.left, val)
        return root

    def print_tree(self, root):
        if root is not None:
            self.print_tree(root.left)
            print(root.val, end=' ')
            self.print_tree(root.right)

    def bfs(self, root):
        if root is None:
            return
        queue = [root]
        while len(queue) > 0:
            print(queue[0].val, end=' ')
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

    def pre_post_inn_order_traversal(self, root):
        pre = []
        inn = []
        post = []
        s = [[root, 1]]
        while len(s) > 0:
            p = s[-1]

            if p[1] == 1:
                s[-1][1] += 1
                pre.append(p[0].val)

                if p[0].left:
                    s.append([p[0].left, 1])
            elif p[1] == 2:
                s[-1][1] += 1
                inn.append(p[0].val)
                if p[0].right:
                    s.append([p[0].right, 1])
            else:
                post.append(p[0].val)
                del s[-1]

        print('Preorder')
        for i in pre:
            print(i, end=' ')
        print('Inorder')
        for i in inn:
            print(i, end=' ')
        print('Postorder')
        for i in post:
            print(i, end=' ')

    # Height of a binary tree. Height of empty tree is -1, height of tree with one node is 0
    def height(self, root):
        if root is None:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def is_balanced(self, root):
        l = self.height(root.left)
        r = self.height(root.roght)
        if abs(l - r) <= 1:
            return True
        return False
