from collections import deque


class newNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def __repr__(self):
        return "value:%s l: (%s) r: (%s)" % (self.val, self.left, self.right)

    # compare two nodes if they are equal
    def __eq__(self, other):
        if self.val == other.val and self.right == other.right and self.left == other.left:
            return True
        else:
            return False


class BinaryTree:
    def __init__(self, val=None):
        # this is necessary when needs to maintain a root with objects
        self.root = newNode(val) if val else None

    # below method inserts data maintaining a root assigned with object of this class
    def insert_witout_root(self, val):
        if not self.root:
            self.root = newNode(val)
            return
        q = [self.root]
        while q:
            n = q.pop(0)
            if not n.left:
                n.left = newNode(val)
                break
            else:
                q.append(n.left)

            if not n.right:
                n.right = newNode(val)
                break
            else:
                q.append(n.right)

    def insert(self, root, val):
        if root is None:
            return newNode(val)

        q = [root]
        while q:
            node = q.pop(0)
            if node.left is None:
                node.left = newNode(val)
                return
            else:
                q.append(node.left)

            if node.right is None:
                node.right = newNode(val)
                return
            else:
                q.append(node.right)

    # DFS traversal goes through depth of tree. DSF is 3 types of
    # such as: inorder, preorder, postorder

    # traversal tree elements in order like: left root right
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.val, end=' ')
        self.inorder(root.right)

    # traversal tree elements in preorder: root left right
    def preorder(self,root):
        if root is None:
            return
        print(root.val, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)

    # traversal tree elements in postorder: left right root
    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val, end=' ')

    # All dfs traversals in one method
    def all_dfs(self, root):

        pre = []
        inn = []
        post = []
        s = [[root, 1]]

        while s:
            n = s[-1]
            if n[1] == 1:
                s[-1][1] += 1
                pre.append(n[0].val)
                if n[0].left:
                    s.append([n[0].left, 1])
            elif n[1] == 2:
                s[-1][1] += 1
                inn.append(n[0].val)
                if n[0].right:
                    s.append([n[0].right, 1])
            else:
                post.append(n[0].val)
                del s[-1]
        print(pre)
        print(inn)
        print(post)

    # BFS traversal
    def bfs(self,root):
        if root is None:
            return
        q = [root]
        while q:
            node = q.pop(0)
            print(node.val,end=' ')
            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

    # Height of a binary tree. Height of empty tree is -1, height of tree with one node is 0
    # TC: O(n)
    # SC: O(n)
    def height(self, root):
        if root is None:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    # Is balanced tree. If the height difference of left and right
    # subtree is <=1 then the tree is balanced
    # TC: O(n)
    # SC: O(n)
    def is_balanced(self, root):
        # Base condition when tree is
        # empty return true
        if root is None:
            return True

        l_height = self.height(root.left)
        r_height = self.height(root.right)
        return abs(l_height - r_height) <= 1

    # The diameter of a tree (sometimes called the width) is the number of nodes on the
    # longest path between any two nodes. It may pass through root or may not.
    # Diameter or width of tree
    # TC: O(n)
    # SC: O(1)
    def diameter(self,root):
        diameter = 0
        def height(root):
            nonlocal diameter
            if root is None:
                return 0
            l = height(root.left)
            r = height(root.right)
            diameter = max(diameter,l+r)
            return max(l,r)+1
        height(root)
        return diameter

    # Find out the path which will give maximum sum
    def max_path_sum(self, root):
        def maxend(node):
            nonlocal maxi
            if not node:
                return 0
            left = maxend(node.left)
            right = maxend(node.right)
            maxi = max(maxi, left + node.val + right)
            return max(node.val + max(left, right), 0)
        maxi = 0
        maxend(root)
        return maxi

    # Check Identical Tree
    def is_identical(self,p,q):
        if not p or not q:
            return p == q
        return (p.val == q.val) and self.is_identical(p.left, q.left) and self.is_identical(p.right, q.right)



# class BinaryTree:
#     def __init__(self, root_key=None):
#         # maps from BinaryTreeNode key to BinaryTreeNode instance.
#         # Thus, BinaryTreeNode keys must be unique.
#         self.nodes = {}
#         if root_key is not None:
#             # create a root BinaryTreeNode
#             self.root = Node(root_key)
#             self.nodes[root_key] = self.root
#
#     def add(self, key, left_key=None, right_key=None):
#         if key not in self.nodes:
#             # BinaryTreeNode with given key does not exist, create it
#             self.nodes[key] = Node(key)
#         # invariant: self.nodes[key] exists
#
#         # handle left child
#         if left_key is None:
#             self.nodes[key].left = None
#         else:
#             if left_key not in self.nodes:
#                 self.nodes[left_key] = Node(left_key)
#             # invariant: self.nodes[left_key] exists
#             self.nodes[key].left = self.nodes[left_key]
#
#         # handle right child
#         if right_key == None:
#             self.nodes[key].right = None
#         else:
#             if right_key not in self.nodes:
#                 self.nodes[right_key] = Node(right_key)
#             # invariant: self.nodes[right_key] exists
#             self.nodes[key].right = self.nodes[right_key]
#
#     def remove(self, key):
#         if key not in self.nodes:
#             raise ValueError('%s not in tree' % key)
#         # remove key from the list of nodes
#         del self.nodes[key]
#         # if node removed is left/right child, update parent node
#         for k in self.nodes:
#             if self.nodes[k].left and self.nodes[k].left.key == key:
#                 self.nodes[k].left = None
#             if self.nodes[k].right and self.nodes[k].right.key == key:
#                 self.nodes[k].right = None
#         return True
#
#     def _height(self, node):
#         if node is None:
#             return 0
#         else:
#             return 1 + max(self._height(node.left), self._height(node.right))
#
#     def height(self):
#         return self._height(self.root)
#
#     def size(self):
#         return len(self.nodes)
#
#     def __repr__(self):
#         return str(self.traverse_inorder(self.root))
#
#     def bfs(self, node):
#         if not node or node not in self.nodes:
#             return
#         reachable = []
#         q = deque()
#         # add starting node to queue
#         q.append(node)
#         while len(q):
#             visit = q.popleft()
#             # add currently visited Node to list
#             reachable.append(visit)
#             # add left/right children as needed
#             if visit.left:
#                 q.append(visit.left)
#             if visit.right:
#                 q.append(visit.right)
#         return reachable
#
#     # visit left child, root, then right child
#     def traverse_inorder(self, node, reachable=None):
#         if not node or node.key not in self.nodes:
#             return
#         if reachable is None:
#             reachable = []
#         self.traverse_inorder(node.left, reachable)
#         reachable.append(node.key)
#         self.traverse_inorder(node.right, reachable)
#         return reachable
#
#     # visit left and right children, then root
#     # root of tree is always last to be visited
#     def traverse_postorder(self, node, reachable=None):
#         if not node or node.key not in self.nodes:
#             return
#         if reachable is None:
#             reachable = []
#         self.traverse_postorder(node.left, reachable)
#         self.traverse_postorder(node.right, reachable)
#         reachable.append(node.key)
#         return reachable
#
#     # visit root, left, then right children
#     # root is always visited first
#     def traverse_preorder(self, node, reachable=None):
#         if not node or node.key not in self.nodes:
#             return
#         if reachable is None:
#             reachable = []
#         reachable.append(node.key)
#         self.traverse_preorder(node.left, reachable)
#         self.traverse_preorder(node.right, reachable)
#         return reachable
