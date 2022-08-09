import math

import tree.binarySearchTree as bst
import tree.binaryTree as bt

b_tree = bst.BinarySearchTree()
root = bst.Node(8)
b_tree.insert(root, 14)
b_tree.insert(root, 18)
b_tree.insert(root, 10)
b_tree.insert(root, 4)
b_tree.insert(root, 7)
b_tree.insert(root, 3)
b_tree.insert(root, 2)
# tree.print_tree(root)
#tree.pre_post_inn_order_traversal(root)

# General tree
tree = bt.BinaryTree()
root = bt.newNode(10)

# root.right = bt.newNode(11)
# root.left = bt.newNode(7)
# root.left.left = bt.newNode(12)
# root.left.right = bt.newNode(9)
# root.left.left.left = bt.newNode(21)
# root.left.left.right = bt.newNode(22)
# root.left.right.left = bt.newNode(9)
# root.left.right.right = bt.newNode(92)
# root.left.right.right.left = bt.newNode(91)
# root.left.right.right.right = bt.newNode(31)


tree.insert(root, 11)
tree.insert(root, 7)
tree.insert(root, 9)
tree.insert(root, 15)
tree.insert(root, 8)

root1 = bt.newNode(10)
tree.insert(root1, 11)
tree.insert(root1, 7)
tree.insert(root1, 9)
tree.insert(root1, 8)
tree.insert(root1, 15)

#tree.inorder(root)
#tree.preorder(root)
#tree.postorder(root)

tree.all_dfs(root)
print(tree.height(root))
print(tree.diameter(root))
print(tree.max_path_sum(root))
print(tree.is_identical(root,root1))

